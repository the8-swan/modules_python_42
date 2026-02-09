# class, def, super(), isinstance(), print(), try/except, list
# comprehensions, from abc import ABC abstractmethod, from typing import Any
# List Dict Union Optional
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_type: str):
        self.stream_type = stream_type
        self.counter = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str]= None) -> List[Any]:
        pass

    # def get_stats(self) -> Dict[str, Union[str, int, float]]:
    #     pass

class SensorStream(DataStream):
    def __init__(self, stream_id):
        print("Initializing Sensor Stream...")
        super().__init__("Environmental Data")
        self.stream_id = f"SENSOR_{stream_id}"
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

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
        	return f"{counter} readings processed, avg temp: {sum(temp)/temp.__len__()}°C"
        else:
        	return f"{counter} readings processed."



    def filter_data(self, data_batch: List[Any],criteria: Optional[str]= None) -> List[Any]:
        pass


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        print("Initializing Transaction Stream...")
        super().__init__("Financial Data")
        self.stream_id = f"TRANS_{stream_id}"
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

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
        except Exception as e :
            print(f"An error occurred while processing the transaction batch:{e}")



class EventStream(DataStream):
    def __init__(self, stream_id):
        print("Initializing Event Stream...")
        super().__init__("System Events")
        self.stream_id = f"EVENT_{stream_id}"
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        error = 0
        for data in data_batch:
            if data == "error":
                error += 1
            self.counter += 1
        return f"{data_batch.__len__()} events, {error} error detected"


class StreamProcessor():
    def __init__(self, streams: List[DataStream]):
        self.streams = streams

    def process_data(self, batches:List[Any]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        for stream, batche in zip(self.streams, batches):
            the_type, lists = batches.items()
            stream.process_batch(lists)
            print(stream.counter)
            


def main():
    data_sensor = [{"temp": 22.5, "humidity":65, "pressure":1013}]
    data_trans = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    data_event = ["login", "error", "logout"]
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Processing sensor batch:", data_sensor)
    sensor = SensorStream(1)
    print(f"Sensor analysis: {sensor.process_batch(data_sensor)}\n")

    print("Processing transaction batch:", data_trans)
    transaction = TransactionStream(1)
    print(f"Transaction analysis:{transaction.process_batch(data_trans)}\n")

    print("Processing Event batch:", data_event)
    event = EventStream(1)
    print(f"Event analysis {event.process_batch(data_event)}")

    batches = {
        "sensor": [{"temp": 8.5}, {"temp": 18.5}],
        "transaction": [{"buy": 19}, {"buy": 93}, {"buy": 87}, {"sell": 10}],
        "event": ["login", "error", "logout"],
    }
    stream = StreamProcessor([sensor, transaction, event])
    stream.process_data(batches)

main()

