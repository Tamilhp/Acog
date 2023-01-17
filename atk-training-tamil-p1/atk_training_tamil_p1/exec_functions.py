from abc import ABC, abstractmethod


class ExecFunction(ABC):
    @abstractmethod
    def __init__(self, options: dict[str, any]):
        pass

    @abstractmethod
    def exec(self, in_record: str) -> str:
        pass


class TransFormUpper(ExecFunction):
    def __init__(self):
        pass

    def exec(self, in_record: str) -> str:
        yield in_record.upper()


class TransFormLower(ExecFunction):
    def __init__(self):
        pass

    def exec(self, in_record: str) -> str:
        yield in_record.lower()


class TransFormRemoveWords(ExecFunction):
    def __init__(self):
        pass

    def exec(self, in_record: str) -> str:
        words = in_record.split()
        stop_words = ["a", "an", "and", "the", "or", "A", "AN", "AND", "THE", "OR"]
        remaining_words = [word for word in words if word not in stop_words]
        yield " ".join(remaining_words)
