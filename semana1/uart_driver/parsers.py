from abc import ABC, abstractmethod

class MessageParser(ABC):
    @abstractmethod
    def can_parse(self, raw_data: bytes) -> bool: ...
    
    @abstractmethod
    def parse(self, raw_data: bytes) -> dict: ...

class ModbusParser(MessageParser):
    def can_parse(self, raw_data: bytes) -> bool:
        return len(raw_data) >= 4
        
    def parse(self, raw_data: bytes) -> dict:
        return {"protocol": "Modbus RTU", "data": raw_data.hex()}

class NMEAParser(MessageParser):
    def can_parse(self, raw_data: bytes) -> bool:
        return raw_data.startswith(b"$GPGGA")
        
    def parse(self, raw_data: bytes) -> dict:
        return {"protocol": "NMEA", "sentence": raw_data.decode('ascii', errors='ignore')}