from typing import Protocol
from dataclasses import dataclass


@dataclass(frozen=True)
class SensorReading:
    sensor_id: str
    value: float


class FatSensorInterface(Protocol):
    def read(self) -> float: ...
    def write(self, value: float) -> None: ...
    def calibrate(self) -> None: ...
    def reset(self) -> None: ...


class Readable(Protocol):
    def read(self) -> float: ...


class Writable(Protocol):
    def write(self, value: float) -> None: ...


class Calibratable(Protocol):
    def calibrate(self) -> None: ...


class SensorSimple:
    def read(self) -> float:
        return 25.0


class PostgreSQLRepository:
    def save(self, reading: SensorReading) -> None:
        pass


class BadDataProcessor:
    def __init__(self) -> None:
        self._repo = PostgreSQLRepository()


class DataRepository(Protocol):
    def save(self, reading: SensorReading) -> None: ...
    def get_latest(self, sensor_id: str) -> SensorReading | None: ...


class DataProcessor:
    """Depende de la abstracción, no de una implementación concreta."""

    def __init__(self, repository: DataRepository) -> None:
        self._repo = repository

    def process(self, reading: SensorReading) -> None:
        self._repo.save(reading)


class InMemoryRepository:
    def __init__(self) -> None:
        self._db: dict[str, SensorReading] = {}

    def save(self, reading: SensorReading) -> None:
        self._db[reading.sensor_id] = reading

    def get_latest(self, sensor_id: str) -> SensorReading | None:
        return self._db.get(sensor_id)
