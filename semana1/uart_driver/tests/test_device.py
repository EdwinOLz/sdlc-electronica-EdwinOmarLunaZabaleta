from semana1.uart_driver.config import UartConfig
from semana1.uart_driver.parsers import NMEAParser
from semana1.uart_driver.device import UartDevice
import pytest

def test_uart_device_levanta_error_si_no_conectado():
    """Verifica que llamar a read_and_parse levante un RuntimeError si el dispositivo no está conectado."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.0)
    parser = NMEAParser()
    device = UartDevice(config=config, parser=parser)

    with pytest.raises(RuntimeError):
        device.read_and_parse(b'$GPGGA,datos')


def test_uart_device_parsea_cuando_esta_conectado():
    """Verifica que al conectar el dispositivo y pasar una trama b'$GPGGA,datos', el método read_and_parse devuelva el diccionario decodificado por el NMEAParser."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.0)
    parser = NMEAParser()
    device = UartDevice(config=config, parser=parser)

    device.connect()
    result = device.read_and_parse(b'$GPGGA,datos')

    assert result['protocol'] == 'NMEA'
    assert result['sentence'] == '$GPGGA,datos'

def test_uart_device_disconnect():
    """Verifica que disconnect() cambie el estado y read_and_parse levante un RuntimeError."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.0)
    parser = NMEAParser()
    device = UartDevice(config=config, parser=parser)

    device.connect()
    device.disconnect()

    with pytest.raises(RuntimeError):
        device.read_and_parse(b'$GPGGA,datos')

def test_uart_device_retorna_none_si_no_puede_parsear():
    """Verifica que retorne None si el NMEAParser no reconoce una trama como b'trama_invalida'."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.0)
    parser = NMEAParser()
    device = UartDevice(config=config, parser=parser)

    device.connect()
    result = device.read_and_parse(b'trama_invalida')

    assert result is None