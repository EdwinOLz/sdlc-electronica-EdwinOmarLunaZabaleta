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