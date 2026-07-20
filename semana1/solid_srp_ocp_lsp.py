from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class SensorReading:
    sensor_id: str
    value: float

# Ejemplo Malo 
class BadAnomalyDetector:
    def __init__(self, threshold: float, tipo_alerta: str) -> None:
        self.threshold = threshold
        self.tipo_alerta = tipo_alerta
    
    def check(self, reading: SensorReading) -> None:
        if reading.value > self.threshold:
            if self.tipo_alerta == "email":
                print(f"Enviando email: Anomalia en {reading.sensor_id}")
            elif self.tipo_alerta == "sms":
                print(f"Enviando SMS: Anomalia en {reading.sensor_id}")
            else:
                print(f"Tipo de alerta desconocido: {self.tipo_alerta}")

# Ejemplo Bueno 
class AlertStrategy(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...

class EmailAlert(AlertStrategy):
    def send(self, message: str) -> None:
        print(f"Enviando email: {message}")
    
class SMSAlert(AlertStrategy):
    def send(self, message: str) -> None:
        print(f"Enviando SMS: {message}")

class AnomalyDetector:
    def __init__(self, alert: AlertStrategy, threshold: float) -> None:
        self._alert = alert
        self._threshold = threshold

    def check(self, reading: SensorReading) -> None:
        if reading.value > self._threshold:
            self._alert.send(f"Anomalia en {reading.sensor_id}")