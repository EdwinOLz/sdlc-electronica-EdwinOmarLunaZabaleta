from typing import Protocol
from dataclasses import dataclass

@dataclass(frozen=True)
class SensorReading:
    sensor_id: str
    value: float

#Mal (tiene muchas funciones que pueden no ser necesarias para todos los sensores)
class FatSensorInterface(Protocol):
    def read(self) -> float: ...
    def write(self, value: float) -> None: ...
    def calibrate(self) -> None: ...
    def reset(self) -> None: ...

#Bien (cada sensor implementa solo lo que necesita)
class Readable(Protocol):
    def read(self) -> float: ...

class Writable(Protocol):
    def write(self, value: float) -> None: ...

class Calibratable(Protocol):
    def calibrate(self) -> None: ...

class SensorSimple:
    def read(self) -> float:
        return 25.0
    
#Mal (depende de una implementacion concreta o real)
class PostgreSQLRepository:
    def save(self, reading: SensorReading) -> None:
        pass 

class BadDataProcessor:
    def __init__(self) -> None:
        self._repo = PostgreSQLRepository()

#Bien (depende de una abstraccion, no de una implementacion concreta)
class DataRepository(Protocol):
    def save(self, reading: SensorReading) -> None: ...
    def get_latest(self, sensor_id: str) -> SensorReading | None: ...

class DataProcessor:
    """Depende de la abstraccion, no de una implementacion concreta."""
    def __init__(self, repository: DataRepository) -> None:
        self._repo = repository 
        
    def process(self, reading: SensorReading) -> None:
        self._repo.save(reading)


# Implementación en memoria para los tests "El pago del DIP"
class InMemoryRepository:
    def __init__(self) -> None:
        self._db: dict[str, SensorReading] = {}
        
    def save(self, reading: SensorReading) -> None:
        self._db[reading.sensor_id] = reading
        
    def get_latest(self, sensor_id: str) -> SensorReading | None:
        return self._db.get(sensor_id)