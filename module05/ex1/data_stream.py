# class, def, super(), isinstance(), print(), try/except, list
# comprehensions, from abc import ABC abstractmethod, from typing import Any
# List Dict Union Optional
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_type: str):
        self.stream_type = stream_type

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
        print("Processing sensor batch:", data_batch)
        temp = []
        counter = 0
        for data in data_batch:
            if "temp" in data:
                if isinstance(data["temp"], (int, float)):
                    temp.append(data["temp"])
                else:
                    print(f"Error : temp value should be a number '{data['temp']}'")
            counter += data.__len__()
        if temp.__len__() != 0:
        	return f"{counter} readings processed, avg temp: {sum(temp)/temp.__len__()}°C"
        else:
        	return f"{counter} readings processed."



    def filter_data(self, data_batch: List[Any],criteria: Optional[str]= None) -> List[Any]:
        pass
#class TransactionStream(DataStream):
#    def __init__(self, stream_id):
#        super().__init__(stream_id, "Financial Data")
#        self.stream_id = f"TRANS_{stream_id}"
#
#
#class EventStream(DataStream):
#    def __init__(self, stream_id):
#        super().__init__(stream_id, "System Events")
#        self.stream_id = f"EVENT_{stream_id}"


#class StreamProcessor():
def main():
    data_sensor = [{"temp":"ho", "humidity":65, "pressure":1013},{"temp":123}]
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream(1)
    print("Sensor analysis:", sensor.process_batch(data_sensor))
main()

