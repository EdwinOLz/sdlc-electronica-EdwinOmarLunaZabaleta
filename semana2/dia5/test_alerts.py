from unittest.mock import MagicMock

from semana2.dia5.alerts import (
    AlertManager,
    AlertStrategy,
    ConsoleAlertStrategy,
    FileAlertStrategy,
)


def test_alert_manager_calls_all_strategies_for_anomaly() -> None:
    console_strategy = MagicMock(spec=AlertStrategy)
    file_strategy = MagicMock(spec=AlertStrategy)

    manager = AlertManager([console_strategy, file_strategy])
    manager.process_anomaly("Temperatura alta")

    console_strategy.send_alert.assert_called_once_with("Temperatura alta")
    file_strategy.send_alert.assert_called_once_with("Temperatura alta")

def test_console_strategy_implements_alert_strategy() -> None:
    strategy = ConsoleAlertStrategy()
    assert isinstance(strategy, AlertStrategy)

def test_file_strategy_implements_alert_strategy() -> None:
    strategy = FileAlertStrategy("alerts.log")
    assert isinstance(strategy, AlertStrategy)