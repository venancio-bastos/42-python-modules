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

    def ingest(self, data: typing.Any) -> None:
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

    def ingest(self, data: typing.Any) -> None:
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

    def ingest(self, data: typing.Any) -> None:
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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        if not data:
            return

        values = [item[1] for item in data]
        print(", ".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        if not data:
            return

        parts = []
        for rank, val in data:
            parts.append(f'"item_{rank}": "{val}"')

        print("{" + ", ".join(parts) + "}")


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
                print(f"DataStream error Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            remaining = len(proc._storage)
            total_processed = proc._processing_rank + remaining
            print(f"{name}: total {total_processed} items processed, remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted = []
            limit = min(nb, len(proc._storage))
            for _ in range(limit):
                try:
                    extracted.append(proc.output())
                except RuntimeError:
                    break

            if extracted:
                plugin.process_output(extracted)


def main() -> None:
    print("=== Code Nexus Data Pipeline ===")
    print("Initialize Data Stream")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch1 = [
        'Hello world', 
        [3.14, 1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch2 = [
        21, 
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},  
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], 
        [32, 42, 64, 84, 128, 168], 
        'World hello'
    ]
    print("Send another batch of data:")
    print(batch2)
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
