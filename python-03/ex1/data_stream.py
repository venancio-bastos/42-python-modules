import typing
import abc

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

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            
            if not processed:
                print(
                    f"DataStream error Can't process element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
            
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            remaining = len(proc._storage)
            total_processed = proc._processing_rank + remaining
            print(
                f"{name}: total {total_processed} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus Data Stream ===")
    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    
    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)
    
    batch1 = [
        'Hello world', 
        [3.14, 1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]
    
    print(f"\nSend first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()
    
    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)
    
    print("Send the same batch again")
    ds.process_stream(batch1)
    ds.print_processors_stats()
    
    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
        
    ds.print_processors_stats()


if __name__ == "__main__":
    main()