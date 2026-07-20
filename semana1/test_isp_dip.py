from semana1.solid_isp_dip import (
    DataProcessor,
    InMemoryRepository,
    SensorReading,
    SensorSimple,
)


def test_sensor_simple_read_con_interfaz_segregada():
    sensor = SensorSimple()

    assert sensor.read() == 25.0


def test_data_processor_guarda_dato_con_repositorio_inyectado():
    repository = InMemoryRepository()
    processor = DataProcessor(repository)
    reading = SensorReading(sensor_id="TEMP-01", value=40.5)

    processor.process(reading)

    assert repository.get_latest("TEMP-01") == reading
