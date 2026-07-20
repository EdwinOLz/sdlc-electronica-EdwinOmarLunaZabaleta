from semana1.uart_driver.recorder import DataRecorder
import json

def test_data_recorder_escribe_json_line(tmp_path):
    """Verifica que DataRecorder escriba un diccionario como una línea JSON en el archivo de texto temporal generado por tmp_path."""
    # Crear un archivo temporal
    file_path = tmp_path / "data.txt"
    recorder = DataRecorder(str(file_path))

    # Datos de prueba
    data = {"key": "value", "number": 42}

    # Llamar al método record
    recorder.record(data)

    # Leer el contenido del archivo y verificar que sea una línea JSON válida
    with open(file_path, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        assert line == json.dumps(data)