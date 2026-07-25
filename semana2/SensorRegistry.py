class SensorNotFoundError(Exception):
    pass

class SensorRegistry:
    def __init__(self) -> None:
        self._sensors: dict[str, str] = {}

    def add(self, sensor_id: str) -> None:
        self._sensors[sensor_id] = sensor_id

    def get(self, sensor_id: str) -> str:
        if sensor_id not in self._sensors:
            raise SensorNotFoundError(f"Sensor {sensor_id} no encontrado")
        
        return self._sensors[sensor_id]