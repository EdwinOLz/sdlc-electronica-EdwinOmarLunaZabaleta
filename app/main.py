from fastapi import FastAPI

from app.db import Base, engine
from app.routers import readings

# Nos aseguramos de que las tablas existan
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SensorHub API", version="0.1.0")

# Conectamos el router 
app.include_router(readings.router)