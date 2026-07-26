from typing import Any

import pytest

from semana2.dia5.sensor_reading import SensorReading


def test_sensor_reading_creates_object_with_float_values() -> None:
    reading = SensorReading(temperature=24.5, humidity=58.2)

    assert reading.temperature == 24.5
    assert reading.humidity == 58.2
    assert isinstance(reading.temperature, float)
    assert isinstance(reading.humidity, float)

@pytest.mark.parametrize(
    ("temperature", "humidity"),
    [("24.5", 58.2), (24.5, "58.2"), (24, 58.2)],
)
def test_sensor_reading_rejects_non_float_values(
    temperature: Any, humidity: Any
) -> None:
    with pytest.raises(TypeError):
        SensorReading(temperature=temperature, humidity=humidity)