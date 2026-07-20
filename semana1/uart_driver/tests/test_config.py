from semana1.uart_driver.config import UartConfig
import pytest
from dataclasses import FrozenInstanceError

def test_uart_config_baudrate_invalido():
    """Verifica que instanciar UartConfig con 1200 baudios levante un ValueError."""
    with pytest.raises(ValueError):
        UartConfig(baudrate=1200, parity='N', stop_bits=1, timeout=1.0)


def test_uart_config_inmutabilidad():
    """Verifica que al intentar cambiar el baudrate de un objeto UartConfig existente se levante un FrozenInstanceError."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.0)
    with pytest.raises(FrozenInstanceError):
        config.baudrate = 9600


def test_uart_config_creacion_exitosa():
    """Verifica que UartConfig se instancie correctamente con un baudrate válido de 115200, paridad 'N', 1 bit de parada y timeout de 1.0."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.0)
    assert config.baudrate == 115200
    assert config.parity == 'N'
    assert config.stop_bits == 1
    assert config.timeout == 1.0