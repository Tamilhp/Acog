from abc import ABC, abstractmethod


class ExecFunction(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def exec(self, in_record: str) -> str:
        pass


class TransFormUpper(ExecFunction):
    """This class takes an input string and returns a capitalized string"""
    def exec(self, in_record: str) -> str:
        return in_record.upper()


class TransFormLower(ExecFunction):
    """This class takes an input string and returns a lower capitalized data string"""
    def exec(self, in_record: str) -> str:
        return in_record.lower()


class TransFormRemoveWords(ExecFunction):
    """This class takes an input string and returns a string without the stop words"""
    def exec(self, in_record: str) -> str:
        words: list[str] = in_record.split()
        stop_words: list[str] = ["a", "an", "and", "the", "or", "A", "AN", "AND", "THE", "OR"]
        remaining_words: list[str] = [word for word in words if word not in stop_words]
        return " ".join(remaining_words)