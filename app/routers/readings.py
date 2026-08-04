from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.sqlalchemy_reading_repository import SQLAlchemyReadingRepository
from app.schemas.reading import ReadingIn, ReadingOut, ReadingUpdate
from app.services.reading_service import ReadingService

# Usamos APIRouter en lugar de FastAPI
router = APIRouter(tags=["readings"])

def get_reading_service(db: Annotated[Session, Depends(get_db)]) -> ReadingService:
    repo = SQLAlchemyReadingRepository(db)
    return ReadingService(repo)

@router.post("/sensors/{sensor_id}/readings", response_model=ReadingOut,
              status_code=status.HTTP_201_CREATED)
def create_reading(
    sensor_id: str, 
    reading: ReadingIn, 
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> Any:
    try:
        return service.record(sensor_id, reading.value, reading.unit)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                             detail=f"Error de validación: {str(e)}") from e

@router.get("/sensors/{sensor_id}/readings", response_model=list[ReadingOut],
             status_code=status.HTTP_200_OK)
def list_readings(
    sensor_id: str,
    service: Annotated[ReadingService, Depends(get_reading_service)],
    limit: int = 50,
    offset: int = 0,
) -> Any:
    # CORRECCIÓN DE CAPAS: Llamamos a un método del servicio, NO al _repo directamente
    return service.list_for_sensor(sensor_id, limit, offset)

@router.get("/readings/{reading_id}", response_model=ReadingOut,
             status_code=status.HTTP_200_OK)
def get_reading(
    reading_id: int,
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> Any:
    reading = service.get_reading(reading_id)
    if not reading:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"La lectura con ID {reading_id} no existe")
    return reading

@router.patch("/readings/{reading_id}", response_model=ReadingOut,
               status_code=status.HTTP_200_OK)
def update_reading(
    reading_id: int,
    update_data: ReadingUpdate,
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> Any:
    reading = service.update_reading(reading_id,
                                      update_data.model_dump(exclude_unset=True))
    if not reading:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se pudo actualizar: Lectura {reading_id} no encontrada")
    return reading

@router.delete("/readings/{reading_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reading(
    reading_id: int,
    service: Annotated[ReadingService, Depends(get_reading_service)]
) -> None:
    success = service.delete_reading(reading_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"No se pudo eliminar: {reading_id} no encontrado")
    return None