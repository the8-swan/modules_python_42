from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str,Any]:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid data input")
        print(f"Input: {data}")
        return data


class TransformStage:
    def process(self, data: Any) -> Dict:
        temp = data["value"]
        if 17 <= data["value"] <= 25:
            data["status"] = "Normal range"
        elif data["value"] < 17:
            data["status"] = "too cold"
        else:
            data["status"] = "too hot"
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return "Output:"


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str,Any]:
        for stage in self.stages[:2]:
            data = stage.process(data)
        
        tmp = data["value"]
        unit = data["unit"]
        message = data["status"]
        return (f"{self.stages[2].process(data)} Processed temperature reading:"
                f"{tmp}°{unit} ({message})"
                )
        


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
    	super().__init__()
    	self.pipeline_id = pipeline_id

    def process(self, data: Any)-> Union[str,Any]:
        for stage in self.stages[:2]:
            data = stage.process(data)

# class StreamAdapter(ProcessingPipeline):
# 	def __init__(self, pipeline_id: int):
# 		super().__init__()
# 		self.pipeline_id = pipeline_id

# 	def process(self, data: Any)-> Any:
# 		pass


class NexusManager:
    def __init__(self):
        print("Initializing Nexus Manager...\n")


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    csv_data = "hellow"
    nexusManager = NexusManager()
    print(
        "Creating Data Processing Pipeline...\n"
        "Stage 1: Input validation and parsing\n"
        "Stage 2: Data transformation and enrichment\n"
        "Stage 3: Output formatting and delivery\n"
    )

    print("=== Multi-Format Data Processing ===\n")
    stages = [InputStage(), TransformStage(), OutputStage()]
    jsonAdapter = JSONAdapter(1)
    csvAdapter = CSVAdapter(1)
    for stage in stages:
        jsonAdapter.add_stage(stage)
        csvAdapter.add_stage(stage)

    print("Processing JSON data through pipeline...")
    result_json = jsonAdapter.process(json_data)
    print("Transform: Parsed and structured data")
    print(f"{result_json}\n")

    print("Processing CSV data through same pipeline...")
    result_csv= csvAdapter.process(csv_data)
    print("Transform: Parsed and structured data")
    //print(f"{result_csv}\n")

    # streamAdapter = StreamAdapter(1)
    # streamAdapter.add_stage(InputStage)
    # streamAdapter.add_stage(TransformStage)
    # streamAdapter.add_stage(OutputStage)


main()
