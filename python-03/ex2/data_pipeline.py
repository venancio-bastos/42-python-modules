import typing
import json
from data_stream import DataStream
from data_processor import NumericProcessor, TextProcessor, LogProcessor


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataPipeline(DataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            data_to_export = []
            for _ in range(nb):
                try:
                    data_to_export.append(proc.output())
                except RuntimeError:
                    break
            
            if data_to_export:
                plugin.process_output(data_to_export)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(", ".join(str(item[1]) for item in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        out_dict = {f"item_{item[0]}": str(item[1]) for item in data}
        print(json.dumps(out_dict))


def main() -> None:
    print("=== Code Nexus Data Pipeline ===")
    print("Initialize Data Stream")
    pipeline = DataPipeline()
    pipeline.print_processors_stats()
    
    print("\nRegistering Processors")
    pipeline.register_processor(NumericProcessor())
    pipeline.register_processor(TextProcessor())
    pipeline.register_processor(LogProcessor())
    
    batch1 = [
        'Hello world', 
        [3.14, 1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]
    
    print(f"\nSend first batch of data on stream: {batch1}")
    pipeline.process_stream(batch1)
    pipeline.print_processors_stats()
    
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    pipeline.output_pipeline(3, csv_plugin)
    pipeline.print_processors_stats()
    
    batch2 = [
        21, 
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
        [{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], 
        [32, 42, 64, 84, 128, 168], 
        'World hello'
    ]
    print(f"\nSend another batch of data:\n{batch2}")
    pipeline.process_stream(batch2)
    pipeline.print_processors_stats()
    
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    pipeline.output_pipeline(5, json_plugin)
    pipeline.print_processors_stats()


if __name__ == "__main__":
    main()
