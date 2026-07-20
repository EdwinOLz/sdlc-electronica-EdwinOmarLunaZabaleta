from dataclasses import dataclass

@dataclass(frozen=True)
class UartConfig:
    baudrate: int
    parity: str
    stop_bits: int
    timeout: float

    def __post_init__(self) -> None:
        if self.baudrate not in (9600, 19200, 38400, 115200):
            raise ValueError(f"Baudrate inválido: {self.baudrate}")