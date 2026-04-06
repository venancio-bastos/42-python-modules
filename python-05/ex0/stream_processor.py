from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data validation failed: Not a numeric list")
            print("Validation: Numeric data verified")

            count = 0
            total = 0
            for num in data:
                total += num
                count += 1
            avg = total / count
            raw_result = (
                f"Processed {count} numeric values, sum={total},"
                f" avg={avg}"
            )
            return self.format_output(raw_result)
        except Exception as e:
            return f"Error processing: {e}"

    def validate(self, data: Any) -> bool:
        if data.__class__ is not list or not data:
            return False
        for i in data:
            if i.__class__ is not [int, float]:
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")
            char_count = 0
            for _ in data:
                char_count += 1
            words = data.split()
            word_count = 0
            for _ in words:
                word_count += 1
            raw_result = (
                f"Processed text: {char_count} characters,"
                " {word_count} words"
                )
            return self.format_output(raw_result)
        except Exception as e:
            return f"Error processing: {e}"

    def validate(self, data: Any) -> bool:
        if data.__class__ is not str or not data:
            return False
        return True


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data.__class__ is not str or ":" not in data:
            return False
        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            parts = data.split(":", 1)
            level = parts[0].strip()
            if parts[1].startswith(" "):
                message = parts[1].strip()
            else:
                message = parts[1]
            prefix = "[ALERT]" if level == "ERROR" else f"[{level}]"

            raw_result = f"{prefix} {level} level detected: {message}"
            return self.format_output(raw_result)
        except Exception as e:
            return f"Error: {e}"


def main() -> None:
    print("CODE NEXUS DATA PROCESSOR FOUNDATION")

    print("\nInitializing Numeric Processor...")
    num_proc = NumericProcessor()
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    if num_proc.validate(data_num):
        print("Validation: Numeric data verified")
    print(num_proc.process(data_num))

    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    data_text = "Hello Nexus World"
    print(f"Processing data: \"{data_text}\"")
    if text_proc.validate(data_text):
        print("Validation: Text data verified")
    print(text_proc.process(data_text))

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    data_log = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_log}\"")
    if log_proc.validate(data_log):
        print("Validation: Log entry verified")
    print(log_proc.process(data_log))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    mixed_data = [
        [1, 2, 3],
        "Data Stream Test",
        "INFO: System ready"
    ]

    count = 1
    for i in range(3):
        res = processors[i].process(mixed_data[i])
        res_limpo = res.replace("Output: ", "")
        print(f"Result {count}: {res_limpo}")
        count += 1


if __name__ == "__main__":
    main()
