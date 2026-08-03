from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db import Base
from app.repositories.sqlalchemy_reading_repository import SQLAlchemyReadingRepository


def test_sqlalchemy_repository_crud() -> None:
    
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    repo = SQLAlchemyReadingRepository(db)
    
    #Probamos que pueda Crear (POST)
    reading = repo.add("TEMP-99", 25.5, "C")
    assert reading.sensor_id == "TEMP-99"
    assert reading.id is not None
    
    #Probamos que pueda Leer por ID (GET)
    fetched = repo.get_by_id(reading.id)
    assert fetched is not None
    assert fetched.value == 25.5
    
    #Probamos que pueda Listar (GET)
    lst = repo.list_for_sensor("TEMP-99")
    assert len(lst) == 1
    
    #Probamos que pueda Actualizar (PATCH)
    repo.update(reading.id, {"value": 30.0})
    updated = repo.get_by_id(reading.id)
    assert updated is not None
    assert updated.value == 30.0
    
    #Probamos que pueda Borrar (DELETE)
    repo.delete(reading.id)
    assert repo.get_by_id(reading.id) is None