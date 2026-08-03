from collections.abc import Generator
from datetime import datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

#Puerto de comunicación físico hacia el archivo SQLite
engine = create_engine("sqlite:///sensorhub.db")

#El canal para abrir/cerrar transacciones ACID
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

#La clase maestra de la que heredan las tablas
class Base(DeclarativeBase):
    pass

#El "molde" o esquema exacto de la tabla relacional
class ReadingModel(Base):
    __tablename__ = "readings"

    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_id: Mapped[str] = mapped_column(index=True)
    value: Mapped[float]
    unit: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
       default=lambda: datetime.now(timezone.utc)
    )

def get_db() -> Generator[Session, None, None]:
    """Generador para inyectar la sesión de base de datos en FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()