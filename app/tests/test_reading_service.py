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
            unit=unit)
        
        self.readings.append(reading)
        self._id_counter += 1
        return reading
        
    def list_for_sensor(self, sensor_id: str) -> list[ReadingModel]:
        return [r for r in self.readings if r.sensor_id == sensor_id]

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