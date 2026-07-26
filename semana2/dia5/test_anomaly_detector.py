from types import SimpleNamespace

from semana2.dia5.anomaly_detector import AnomalyDetector


def test_detects_temperature_anomaly() -> None:
    detector = AnomalyDetector(max_temperature=30.0, max_humidity=70.0)
    reading = SimpleNamespace(temperature=31.5, humidity=60.0)
    assert detector.is_anomaly(reading) is True

def test_detects_humidity_anomaly() -> None:
    detector = AnomalyDetector(max_temperature=30.0, max_humidity=70.0)
    reading = SimpleNamespace(temperature=29.0, humidity=71.2)
    assert detector.is_anomaly(reading) is True

def test_returns_false_for_normal_reading() -> None:
    detector = AnomalyDetector(max_temperature=30.0, max_humidity=70.0)
    reading = SimpleNamespace(temperature=25.0, humidity=65.0)
    assert detector.is_anomaly(reading) is False