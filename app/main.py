from datetime import datetime
from typing import Annotated, Any

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.sqlalchemy_reading_repository import SQLAlchemyReadingRepository
from app.services.reading_service import ReadingService

app = FastAPI(title="SensorHub API", version="0.1.0")

#Esquemas de Validación (Pydantic)
class ReadingIn(BaseModel):
    value: float
    unit: str = Field(default="C")

class ReadingOut(BaseModel):
    id: int
    sensor_id: str
    value: float
    unit: str
    created_at: datetime
    
    class Config:
        from_attributes = True  #Permite convertir a JSON automáticamente

class ReadingUpdate(BaseModel):
    value: float | None = None
    unit: str | None = None

#El Inyector de Dependencias
def get_reading_service(db: Annotated[Session, Depends(get_db)]) -> ReadingService:
    """Instancia el repositorio real y el servicio, inyectando la sesión de DB."""
    repo = SQLAlchemyReadingRepository(db)
    return ReadingService(repo)

@app.post(
"/sensors/{sensor_id}/readings",
response_model=ReadingOut,
status_code=status.HTTP_201_CREATED)
def create_reading(
    sensor_id: str, 
    reading: ReadingIn, 
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> Any:
    try:
        # Llamamos a la lógica de negocio (que incluye la validación del cero absoluto)
        return service.record(sensor_id,
        reading.value, reading.unit)
    except ValueError as e:
        # Si la física falla, lanzamos el código 422 (Unprocessable Entity)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=str(e)) from e

@app.get("/sensors/{sensor_id}/readings",
         response_model=list[ReadingOut],
         status_code=status.HTTP_200_OK)
def list_readings(
    sensor_id: str,
    service: Annotated[ReadingService, Depends(get_reading_service)],
    limit: int = 50,
    offset: int = 0,
) -> Any:
    # Usamos los parámetros de consulta (limit, offset) para la paginación
    return service._repo.list_for_sensor(sensor_id, limit, offset)

@app.get("/readings/{reading_id}", response_model=ReadingOut, 
         status_code=status.HTTP_200_OK)
def get_reading(
    reading_id: int,
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> Any:
    reading = service.get_reading(reading_id)
    if not reading:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Lectura no encontrada")
    return reading

@app.patch("/readings/{reading_id}", response_model=ReadingOut,
            status_code=status.HTTP_200_OK)
def update_reading(
    reading_id: int,
    update_data: ReadingUpdate,
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> Any:
    # exclude_unset=True asegura que solo actualicemos los campos que el usuario envió
    reading = service.update_reading(reading_id, 
                                     update_data.model_dump(exclude_unset=True))
    if not reading:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Lectura no encontrada")
    return reading

@app.delete("/readings/{reading_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reading(
    reading_id: int,
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> None:
    success = service.delete_reading(reading_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Lectura no encontrada")
    return None