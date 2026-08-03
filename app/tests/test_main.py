from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_reading_service
from app.services.reading_service import ReadingService
from app.tests.test_reading_service import FakeReadingRepository

client = TestClient(app)

def override_get_reading_service() -> ReadingService:
    fake_repo = FakeReadingRepository()
    return ReadingService(fake_repo)

app.dependency_overrides[get_reading_service] = override_get_reading_service

#Las Pruebas de Integración

def test_create_valid_reading() -> None:
    response = client.post(
        "/sensors/TEMP-01/readings", 
        json={"value": 25.0, "unit": "C"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["sensor_id"] == "TEMP-01"
    assert data["value"] == 25.0

def test_create_invalid_reading_absolute_zero() -> None:
    response = client.post(
        "/sensors/TEMP-01/readings", 
        json={"value": -300.0, "unit": "C"}
    )
    # Debe ser atrapado y devuelto como Unprocessable Entity
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    assert "cero absoluto" in response.json()["detail"]

def test_list_readings_empty() -> None:
    response = client.get("/sensors/TEMP-02/readings")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_reading_not_found() -> None:
    response = client.get("/readings/999")
    assert response.status_code == 404

def test_update_reading_not_found() -> None:
    response = client.patch("/readings/999", json={"value": 10.0})
    assert response.status_code == 404

def test_delete_reading_not_found() -> None:
    response = client.delete("/readings/999")
    assert response.status_code == 404