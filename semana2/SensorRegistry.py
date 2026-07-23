class SensorNotFoundError(Exception):
    pass

class SensorRegistry:
    def get(self, sensor_id: str):
        raise SensorNotFoundError(f"Sensor {sensor_id} no encontrado")