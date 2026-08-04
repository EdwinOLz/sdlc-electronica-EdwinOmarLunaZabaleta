from app.db import ReadingModel
from app.repositories.reading_repository import ReadingRepository


class ReadingService:
    """Lógica de negocio. Depende de la abstracción del repositorio (DIP)."""
    
    def __init__(self, repo: ReadingRepository) -> None:
        self._repo = repo
        
    def record(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        if value < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        return self._repo.add(sensor_id, value, unit)

    # NUEVO MÉTODO: El servicio expone la lista para que el router no llame a _repo
    def list_for_sensor(self, sensor_id: str, limit: int = 50, 
                        offset: int = 0) -> list[ReadingModel]:
        return self._repo.list_for_sensor(sensor_id, limit, offset)

    def get_reading(self, reading_id: int) -> ReadingModel | None:
        return self._repo.get_by_id(reading_id)

    def update_reading(self, reading_id: int, data: dict) -> ReadingModel | None:
        return self._repo.update(reading_id, data)

    def delete_reading(self, reading_id: int) -> bool:
        return self._repo.delete(reading_id)