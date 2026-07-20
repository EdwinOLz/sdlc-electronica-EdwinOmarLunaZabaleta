from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol

class SensorType(Enum):
    TEMPERATURE = auto()
    HUMIDITY = auto()

@dataclass(frozen=True)
class Reading:
    sensor_id: str
    value: float
    sensor_type: SensorType

class Transport(Protocol):
    def send(self, payload: bytes) -> None: ...

def to_frame(r: Reading) -> bytes:
    return f"{r.sensor_id}:{r.value:.2f}".encode()

# 1.Celsius a Fahrenheit
def convertir_a_fahrenheit(r: Reading) -> Reading:
    grados_fahrenheit = (r.value * 9/5) + 32
    
    nuevos_valores = Reading(
        sensor_id=r.sensor_id, 
        value=grados_fahrenheit, 
        sensor_type=r.sensor_type
    )
    
    return nuevos_valores

# 2.Detección de umbral (alarma)
def supera_umbral(r: Reading, limite: float) -> bool:
    if r.value > limite:
        return True
    else:
        return False
    

# 3.Serialización a JSON
def a_json(r: Reading) -> str:
    JSON = f'{{"sensor_id": "{r.sensor_id}", "value": {r.value:.2f}, "sensor_type": "{r.sensor_type.name}"}}'
    return JSON

# 4.Aplicación de un offset 
def calibrar_offset(r: Reading, offset: float) -> Reading:
    valor_ajustado = r.value + offset
    
    nuevos_valores = Reading(
        sensor_id=r.sensor_id, 
        value=valor_ajustado, 
        sensor_type=r.sensor_type
    )
    
    return nuevos_valores

# 5.Validación de rango operativo
def es_lectura_valida(r: Reading, min_val: float, max_val: float) -> bool:
    if min_val <= r.value <= max_val:
        return True
    else:
        return False