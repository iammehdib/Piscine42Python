import typing
import abc


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool: ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None: ...

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")

        oldest_data: str = self._storage[0]
        rank: int = self._rank

        self._storage.pop(0)
        self._rank += 1

        return rank, oldest_data


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
            return True

        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for value in data:
                self._storage.append(str(value))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            for value in data:
                if not isinstance(value, str):
                    return False
            return True

        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for value in data:
                self._storage.append(value)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        elif isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                for key, value in d.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            self._storage.append(f"{data['log_level']}: {data['log_message']}")
            return
        for d in data:
            self._storage.append(f"{d['log_level']}: {d['log_message']}")


if __name__ == '__main__':
    print('=== Code Nexus - Data Processor ===')
    print()

    print('Testing Numeric Processor...')
    numeric = NumericProcessor()
    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(f" Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')  # type: ignore
    except ValueError as e:
        print(f"  Got exception: {e}")
    data_num: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    numeric.ingest(data_num)
    print(" Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print(f"  Numeric value {rank}: {value}")
    print()

    print('Testing Text Processor...')
    text = TextProcessor()
    print(f" Trying to validate input '42': {text.validate(42)}")
    data_text = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data_text}")
    text.ingest(data_text)
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f"  Text value {rank}: {value}")
    print()

    print('Testing Log Processor...')
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data_log}")
    log.ingest(data_log)
    print(" Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f"  Log entry {rank}: {value}")
