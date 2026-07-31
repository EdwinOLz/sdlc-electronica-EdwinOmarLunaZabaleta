from app.repositories.reading_repository import ReadingRepository
from app.db import ReadingModel

class ReadingService:
    """Logica de negocio. Depende de la abstraccion del repositorio (DIP)."""
    
    def __init__(self, repo: ReadingRepository) -> None:
        self._repo = repo
        
    def record(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        if value < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        return self._repo.add(sensor_id, value, unit)