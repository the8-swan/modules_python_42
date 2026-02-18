from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_type: str) -> Any:
        self.stream_type = stream_type
        self.counter = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if item == criteria]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"ID": self.stream_id, "Type": self.stream_type}


class SensorStream(DataStream):
    def __init__(self, stream_id: int) -> Any:
        super().__init__("Environmental Data")
        self.stream_id = f"SENSOR_{stream_id}"

    def process_batch(self, data_batch: List[Any]) -> str:
        temp = []
        counter = 0
        for data in data_batch:
            if "temp" in data:
                if isinstance(data["temp"], (int, float)):
                    temp.append(data["temp"])
                else:
                    print(f"Error : temp value should be a number '{data['temp']}'")
            counter += data.__len__()
            self.counter += 1
        if temp.__len__() != 0:
            return (
                f"{counter} readings processed, avg temp: {sum(temp)/temp.__len__()}°C"
            )
        else:
            return f"{counter} readings processed."

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch if criteria == "high_temp" and item["temp"] > 22
        ]


class TransactionStream(DataStream):
    def __init__(self, stream_id: int) -> Any:
        super().__init__("Financial Data")
        self.stream_id = f"TRANS_{stream_id}"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buy = 0
            sell = 0
            for data in data_batch:
                for action, num in data.items():
                    if action == "buy":
                        buy += num
                    if action == "sell":
                        sell += num
                    self.counter += 1
            result = buy - sell
            return f"{len(data_batch)} operations, net flow: {'+' if result > 0 else ''}{result}"
        except Exception as e:
            print(f"An error occurred while processing the transaction batch:{e}")

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item
            for item in data_batch
            if criteria == "large_trans" and item["buy"] > 150
        ]


class EventStream(DataStream):
    def __init__(self, stream_id: int) -> Any:
        super().__init__("System Events")
        self.stream_id = f"EVENT_{stream_id}"

    def process_batch(self, data_batch: List[Any]) -> str:
        error = 0
        for data in data_batch:
            if data == "error":
                error += 1
            self.counter += 1
        return f"{data_batch.__len__()} events, {error} error detected"


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> Any:
        self.streams = streams

    def process_data(self, batches: dict) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        for stream, batche in zip(self.streams, batches.values()):
            stream.process_batch(batche)
            if isinstance(stream, SensorStream):
                print(f"-Sensor data: {stream.counter} readings processed")
            if isinstance(stream, TransactionStream):
                print(f"-Transaction data: {stream.counter} operations processed")
            if isinstance(stream, EventStream):
                print(f"-Event data: {stream.counter} events processed")
        print("")

    def apply_filter(self) -> Any:
        print("Stream filtering active: High-priority data only")
        temp = self.streams[0].filter_data(
            [{"temp": 23.0}, {"temp": 26.0}], "high_temp"
        )
        transaction = self.streams[1].filter_data(
            [{"buy": 19}, {"buy": 193}], "large_trans"
        )
        print(
            f"Filtered results: {len(temp)} critical sensor alerts,"
            f" {len(transaction)} large transaction.\n"
        )


def main() -> Any:
    data_sensor = [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    data_trans = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    data_event = ["login", "error", "logout"]
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream(1)
    data = sensor.get_stats()
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {data['ID']}, Type: {data['Type']}")
    print("Processing sensor batch:", data_sensor)
    print(f"Sensor analysis: {sensor.process_batch(data_sensor)}\n")

    transaction = TransactionStream(1)
    data = transaction.get_stats()
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {data['ID']}, Type: {data['Type']}")
    print("Processing transaction batch:", data_trans)
    print(f"Transaction analysis:{transaction.process_batch(data_trans)}\n")

    event = EventStream(1)
    data = event.get_stats()
    print("Initializing Event Stream...")
    print(f"Stream ID: {data['ID']}, Type: {data['Type']}")
    print("Processing Event batch:", data_event)
    print(f"Event analysis {event.process_batch(data_event)}\n")

    batches = {
        "sensor": [{"temp": 8.5}, {"temp": 18.5}],
        "transaction": [{"buy": 19}, {"buy": 93}, {"buy": 87}, {"sell": 10}],
        "event": ["login", "error", "logout"],
    }
    stream = StreamProcessor([SensorStream(2), TransactionStream(2), EventStream(1)])
    stream.process_data(batches)
    stream.apply_filter()
    print("All streams processed successfully. Nexus throughput optimal.")


main()
