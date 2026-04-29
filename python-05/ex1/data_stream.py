import typing
from data_processor import DataProcessor, NumericProcessor, TextProcessor, LogProcessor


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
            print(
                f"{name}: total {total_processed} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus Data Stream ===")
    print("Initialize Data Stream..")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor")
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

    print(f"Send first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    print("Send the same batch again")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
