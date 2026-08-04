from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ReadingIn(BaseModel):
    # Agregamos validación física real: ge=-273.15 (cero absoluto)
    value: float = Field(..., ge=-273.15, description="Valor físico de la lectura")
    # Restringimos a unidades reales conocidas
    unit: str = Field(default="C", pattern="^(C|F|K|%)$",
                       description="Unidad de medida (C, F, K, %)")

class ReadingOut(BaseModel):
    id: int
    sensor_id: str
    value: float
    unit: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class ReadingUpdate(BaseModel):
    value: float | None = Field(default=None, ge=-273.15)
    unit: str | None = Field(default=None, pattern="^(C|F|K|%)$")