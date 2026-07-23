import abc
import typing


class DataProcessor(abc.ABC):

    name: str = "Data Processor"

    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0
        self._total: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool: ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None: ...

    def _store(self, value: str) -> None:
        self._storage.append(value)
        self._total += 1

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")

        oldest_data: str = self._storage.pop(0)
        rank: int = self._rank
        self._rank += 1
        return rank, oldest_data

    def remaining(self) -> int:
        return len(self._storage)

    def total(self) -> int:
        return self._total


class NumericProcessor(DataProcessor):

    name = "Numeric Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(value, (int, float)) for value in data)
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for value in data:
                self._store(str(value))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):

    name = "Text Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(value, str) for value in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for value in data:
                self._store(value)
        else:
            self._store(data)


class LogProcessor(DataProcessor):

    name = "Log Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) and isinstance(value, str)
                       for key, value in data.items())
        if isinstance(data, list):
            return all(self.validate(entry) for entry in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            self._store(f"{data['log_level']}: {data['log_message']}")
            return
        for entry in data:
            self._store(f"{entry['log_level']}: {entry['log_message']}")


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process element "
                      f"in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total()} items processed, "
                  f"remaining {proc.remaining()} on processor")


if __name__ == '__main__':
    print('=== Code Nexus - Data Stream ===')
    print('Initialize Data Stream...')
    stream = DataStream()
    stream.print_processors_stats()

    print()
    print('Registering Numeric Processor')
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five'],
    ]

    print()
    print(f'Send first batch of data on stream: {batch}')
    stream.process_stream(batch)
    stream.print_processors_stats()

    print()
    print('Registering other data processors')
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print('Send the same batch again')
    stream.process_stream(batch)
    stream.print_processors_stats()

    print()
    print('Consume some elements from the data processors: '
          'Numeric 3, Text 2, Log 1')
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    stream.print_processors_stats()
