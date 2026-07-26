from typing import Any


class AnomalyDetector:
    def __init__(self, max_temperature: float, max_humidity: float) -> None:
        self.max_temperature = max_temperature
        self.max_humidity = max_humidity

    def is_anomaly(self, reading: Any) -> bool:
        return (
            reading.temperature > self.max_temperature
            or reading.humidity > self.max_humidity
        )