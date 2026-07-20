import json

class DataRecorder:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def record(self, data: dict) -> None:
        with open(self._file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(data) + "\n")