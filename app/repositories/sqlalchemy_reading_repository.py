from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import ReadingModel


class SQLAlchemyReadingRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, sensor_id: str, value: float, unit: str) -> ReadingModel:
        reading = ReadingModel(
            sensor_id=sensor_id, 
            value=value, 
            unit=unit,
        )
        self._session.add(reading)
        self._session.commit()
        self._session.refresh(reading)
        return reading

    def list_for_sensor(
        self, sensor_id: str,
        limit: int = 50,
        offset: int = 0) -> list[ReadingModel]:

        stmt = select(ReadingModel).where(
            ReadingModel.sensor_id == sensor_id
        ).offset(offset).limit(limit)
        return list(self._session.scalars(stmt).all())

    def get_by_id(self, reading_id: int) -> ReadingModel | None:
        return self._session.get(ReadingModel, reading_id)

    def update(self, reading_id: int, data: dict) -> ReadingModel | None:
        reading = self.get_by_id(reading_id)
        if reading:
            for key, value in data.items():
                setattr(reading, key, value)
            self._session.commit()
            self._session.refresh(reading)
        return reading

    def delete(self, reading_id: int) -> bool:
        reading = self.get_by_id(reading_id)
        if reading:
            # En producción se recomienda desactivar, pero para el CRUD base lo borramos
            self._session.delete(reading)
            self._session.commit()
            return True
        return False