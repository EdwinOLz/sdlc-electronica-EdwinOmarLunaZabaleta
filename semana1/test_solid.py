from semana1.solid_srp_ocp_lsp import SensorReading, AnomalyDetector
class FakeAlert:
    def __init__(self):
        self.messages = []

    def send(self, message: str) -> None:
        self.messages.append(message)


def test_envia_mensaje_si_el_sensor_supera_el_threshold():
    alert = FakeAlert()
    detector = AnomalyDetector(alert=alert, threshold=10)
    reading = SensorReading(sensor_id="TEMP-01", value=15)

    detector.check(reading)

    assert alert.messages == ["Anomalia en TEMP-01"]


def test_no_envia_mensaje_si_el_sensor_no_supera_el_threshold():
    alert = FakeAlert()
    detector = AnomalyDetector(alert=alert, threshold=10)
    reading = SensorReading(sensor_id="TEMP-01", value=10)

    detector.check(reading)

    assert alert.messages == []

