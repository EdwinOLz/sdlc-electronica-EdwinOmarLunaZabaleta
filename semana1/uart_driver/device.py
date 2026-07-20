from semana1.uart_driver.config import UartConfig
from semana1.uart_driver.parsers import MessageParser

class UartDevice:
    def __init__(self, config: UartConfig, parser: MessageParser) -> None:
        self._config = config
        self._parser = parser
        self._is_connected = False

    def connect(self) -> None:
        self._is_connected = True
        
    def disconnect(self) -> None:
        self._is_connected = False
        
    def read_and_parse(self, raw_data: bytes) -> dict | None:
        if not self._is_connected:
            raise RuntimeError("El dispositivo no está conectado.")
            
        if self._parser.can_parse(raw_data):
            return self._parser.parse(raw_data)
        return None