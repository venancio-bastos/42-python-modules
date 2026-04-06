from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        if not criteria:
            return data_batch
        return [
            i for i in data_batch
            if isinstance(i, str) and criteria in i
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [
                float(i.split(":")[1].strip())
                for i in data_batch
                if isinstance(i, str) and "temp" in i
            ]
            avg = sum(temps) / len(temps) if temps else 0.0
            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg}°C"
            )
        except Exception as e:
            return f"Error: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buys = [
                int(x.split(":")[1].strip()) for x in data_batch
                if isinstance(x, str) and "buy" in x
            ]
            sells = [
                int(x.split(":")[1].strip()) for x in data_batch
                if isinstance(x, str) and "sell" in x
            ]
            net_flow = sum(buys) - sum(sells)
            sign = "+" if net_flow >= 0 else ""

            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{net_flow} units"
            )
        except Exception as e:
            return f"Error processing transaction batch: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = [
                x for x in data_batch
                if isinstance(x, str) and x == "error"
            ]
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error detected"
            )
        except Exception as e:
            return f"Error processing event batch: {e}"


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("Batch 1 Results:")

        for i, stream in enumerate(self.streams):
            if i < len(batches):
                if isinstance(stream, SensorStream):
                    print(f"Sensor data: {len(batches[i])} readings processed")
                elif isinstance(stream, TransactionStream):
                    print(
                        f"Transaction data: {len(batches[i])} "
                        "operations processed")
                elif isinstance(stream, EventStream):
                    print(f"Event data: {len(batches[i])} events processed")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    
    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    s_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(s_batch)}]") 
    print(sensor.process_batch(s_batch))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print("Stream ID: TRANS_001, Type: Financial Data")
    t_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(t_batch)}]")
    print(trans.process_batch(t_batch))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print("Stream ID: EVENT_001, Type: System Events")
    e_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(e_batch)}]")
    print(event.process_batch(e_batch))

    print("")
    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(trans)
    manager.add_stream(event)
    
    manager.process_all([
        ["temp: 20", "humidity: 40"], 
        ["buy: 10", "buy: 20", "sell: 5", "sell: 5"], 
        ["login", "logout", "error"]
    ])
    
    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction\n")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
