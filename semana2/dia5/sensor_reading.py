from dataclasses import dataclass


@dataclass
class SensorReading:
    temperature: float
    humidity: float

    def __post_init__(self) -> None:
        if not isinstance(self.temperature, float):
            raise TypeError("temperature must be a float")
        if not isinstance(self.humidity, float):
            raise TypeError("humidity must be a float")