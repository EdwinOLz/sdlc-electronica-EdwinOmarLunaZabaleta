import pytest

from semana2.SensorRegistry import SensorNotFoundError, SensorRegistry


def test_get_unknown_sensor_raises() -> None:
    registry = SensorRegistry()
    with pytest.raises(SensorNotFoundError):
        registry.get("GHOST-99")

def test_get_existing_sensor_returns_sensor() -> None:
    registry = SensorRegistry()
    registry.add("TEMP-01") 
    sensor = registry.get("TEMP-01")
    assert sensor == "TEMP-01"