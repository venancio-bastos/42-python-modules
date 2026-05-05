import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._processing_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise RuntimeError("No data available to output.")

        extracted_data = self._storage.pop(0)
        current_rank = self._processing_rank
        self._processing_rank += 1

        return current_rank, extracted_data


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            return all(type(x) in (int, float) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        def is_valid_dict(d: typing.Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(log_entry: dict[str, str]) -> str:
            if "log_level" in log_entry and "log_message" in log_entry:
                return f"{log_entry['log_level']}: {log_entry['log_message']}"
            return ", ".join(f"{k}: {v}" for k, v in log_entry.items())

        if isinstance(data, list):
            for item in data:
                self._storage.append(format_log(item))
        else:
            self._storage.append(format_log(data))


def main() -> None:
    print("=== Code Nexus Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # type: ignore [cite: 390-391]
    except Exception as e:
        print(f"Got exception: {e}")

    test_data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {test_data_num}")
    num_proc.ingest(test_data_num)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    test_data_text = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {test_data_text}")
    text_proc.ingest(test_data_text)

    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    test_data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!!'}
    ]
    print(f"Processing data: {test_data_log}")
    log_proc.ingest(test_data_log)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
