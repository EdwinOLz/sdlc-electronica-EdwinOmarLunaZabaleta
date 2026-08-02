from typing import Protocol

from app.db import ReadingModel


class ReadingRepository(Protocol):
    def add(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        ...
    
    def list_for_sensor(self, sensor_id: str, limit: int = 50,
                         offset: int = 0) -> list[ReadingModel]:
        ...

    def get_by_id(self, reading_id: int) -> ReadingModel | None:
        ...

    def update(self, reading_id: int, data: dict) -> ReadingModel | None:
        ...
        
    def delete(self, reading_id: int) -> bool:
        ...