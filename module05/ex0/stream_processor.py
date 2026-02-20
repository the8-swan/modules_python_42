from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> Any:
        pass

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                if isinstance(d, (int, float)) is False:
                    return False
            return True
        else:
            return False

    def process(self, data: Any) -> str:
        summ: int = sum(data[0:])
        length: int = len(data)
        return (f"processed {length} numeric values, sum={summ} ,"
                f" avg ={summ/length}")


class TextProcessor(DataProcessor):
    def __init__(self) -> Any:
        pass

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is False:
            return False
        return True

    def process(self, data: Any) -> str:
        return (f"Processed text: {len(data)} characters,"
                f" {len(data.split())} words")


class LogProcessor(DataProcessor):
    def __init__(self) -> Any:
        pass

    def validate(self, data: Any) -> bool:
        if data.startswith("ERROR") or data.startswith("INFO"):
            return True
        return False

    def process(self, data: Any) -> str:
        text, info = data.split(":")
        if text == "ERROR":
            return f"[ALERT] {text} level detected:{info}"
        else:
            return f"[INFO] {text} level detected:{info}"


def main():
    numeric = [1, 2, 3, 4, 5]
    text = "Hello Nexus World"
    log = "ERROR: Connection timeout"
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # number processing
    print("Initializing Numeric Processor...")
    numericProcessor = NumericProcessor()
    print(f"Processing data: {numeric}")
    if numericProcessor.validate(numeric):
        print("Validation: Numeric data verified")
        print(f"Output: {numericProcessor.process(numeric)}\n")
    else:
        print("Validaiton: not all data is numbers \n")
    print("")

    # text processing
    print("Initializing Text Processor...")
    textProcessor = TextProcessor()
    print("Processing data:", text)
    if textProcessor.validate(text):
        print("Validation: Text data verified")
        print(f"Output: {textProcessor.process(text)}\n")
    else:
        print("Validaiton: the data should be a string\n")

    # Log processor
    print("Initializing Log Processor...")
    print(f"Processing data: {log}")
    logProcessor = LogProcessor()
    if logProcessor.validate(log):
        print("Validation: Log entry verified")
        print(f"Output: {logProcessor.process(log)}\n")
    else:
        print("Validation: Log entry is unvalid \n")

    # Polymorphic Processing
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    objects = [numericProcessor, textProcessor, logProcessor]
    data = [[1, 2, 3], "hello world!", "INFO:  System ready"]

    for o, d in zip(objects, data):
        result = o.process(d)
        print(f"{o.format_output(result)}")
    print("")
    print("Foundation systems online. Nexus ready for advanced streams.")


main()
