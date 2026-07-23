import pytest
from semana2.SensorRegistry import SensorRegistry, SensorNotFoundError

def test_get_unknown_sensor_raises():
    registry = SensorRegistry()
    with pytest.raises(SensorNotFoundError):
        registry.get("GHOST-99")

def test_get_existing_sensor_returns_sensor():
    registry = SensorRegistry()
    registry.add("TEMP-01") 
    sensor = registry.get("TEMP-01")
    assert sensor == "TEMP-01"