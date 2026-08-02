import pytest

from app.db import ReadingModel
from app.services.reading_service import ReadingService


#Repositorio Fake 
class FakeReadingRepository:
    def __init__(self) -> None:
        self.readings: list[ReadingModel] = []
        self._id_counter = 1

    def add(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        reading = ReadingModel(
            id=self._id_counter, 
            sensor_id=sensor_id, 
            value=value, 
            unit=unit,
            created_at=datetime.utcnow()  # <- Esto soluciona el error
        )
        self.readings.append(reading)
        self._id_counter += 1
        return reading
        
    def list_for_sensor(self, sensor_id: str,
                         limit: int = 50, offset: int = 0) -> list[ReadingModel]:
        resultados = [r for r in self.readings if r.sensor_id == sensor_id]
        return resultados[offset : offset + limit]

    def get_by_id(self, reading_id: int) -> ReadingModel | None:
        return next((r for r in self.readings if r.id == reading_id), None)

    def update(self, reading_id: int, data: dict) -> ReadingModel | None:
        reading = self.get_by_id(reading_id)
        if reading:
            for k, v in data.items():
                setattr(reading, k, v)
        return reading

    def delete(self, reading_id: int) -> bool:
        reading = self.get_by_id(reading_id)
        if reading:
            self.readings.remove(reading)
            return True
        return False

#Tests Unitarios

def test_record_valid_reading() -> None:
    # Preparamos el entorno inyectando el simulador
    fake_repo = FakeReadingRepository()
    service = ReadingService(repo=fake_repo)
    
    # Ejecutamos la lógica de negocio
    result = service.record("TEMP-01", 25.0, "C")
    
    # Comprobamos que el servicio y el repositorio se comunicaron bien
    assert result.sensor_id == "TEMP-01"
    assert result.value == 25.0
    assert len(fake_repo.readings) == 1

def test_record_invalid_temperature() -> None:
    fake_repo = FakeReadingRepository()
    service = ReadingService(repo=fake_repo)
    
    # Comprobamos que el servicio detecta y rechaza la física imposible
    with pytest.raises(ValueError, match="Temperatura por debajo del cero absoluto"):
        service.record("TEMP-01", -300.0, "C")