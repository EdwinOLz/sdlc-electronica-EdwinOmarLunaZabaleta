from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class AlertStrategy(ABC):
    @abstractmethod
    def send_alert(self, message: str) -> None:
        raise NotImplementedError

class ConsoleAlertStrategy(AlertStrategy):
    def send_alert(self, message: str) -> None:
        print(message)

class FileAlertStrategy(AlertStrategy):
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

    def send_alert(self, message: str) -> None:
        with self.file_path.open("a", encoding="utf-8") as handle:
            handle.write(message + "\n")

class AlertManager:
    def __init__(self, strategies: list[AlertStrategy]) -> None:
        self.strategies = strategies

    def process_anomaly(self, message: str) -> None:
        for strategy in self.strategies:
            strategy.send_alert(message)