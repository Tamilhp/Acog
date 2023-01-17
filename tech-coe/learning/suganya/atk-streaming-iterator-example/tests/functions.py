# Uses iterator to convert the iterator(can be a list or tuple) of records into upper case
from typing import Iterator, Dict, Any
from abc import ABC, abstractmethod
import re

class TransformFunctions(ABC):
    def __init__(self, from_dict: Dict[str, Any] = None):
        pass

    @abstractmethod
    def __call__(self, in_record: str) -> str:
        pass


class TransformToUpper(TransformFunctions):
    ''' Convert the iterator(can be a list or tuple) of records into upper case '''
    def __call__(input_stream: Iterator[str]) -> Iterator[str]:
        for r in input_stream:
                up_r = r.upper()
                yield up_r

class TransformToLower(TransformFunctions):
    ''' Convert the iterator(can be a list or tuple) of records into upper case '''
    def __call__(input_stream: Iterator[str]) -> Iterator[str]:
        for r in input_stream:
                up_r = r.lower()
                yield up_r

class TransformToCapitalize(TransformFunctions):
    ''' Uses iterator to convert the iterator(can be a list or tuple) of records into captialized form '''
    def __call__(input_stream: Iterator[str]) -> Iterator[str]:
        for r in input_stream:
                capitalized_r = r.capitalize()
                yield capitalized_r

class TransformMultiplelinesToSingle(TransformFunctions):
    ''' Uses iterator to convert multiple empty lines to single empty line '''
    def __call__(input_stream: Iterator[str]) -> Iterator[str]:
        prev_record=''
        for r in input_stream:
            if r.strip() == "":
                pass
            else:
                prev_record = r
                yield r

class TransformToLessCharacters(TransformFunctions):
    ''' Users iterator to convert line into multiple lines with each line having less than 25 characters '''
    def __call__(input_stream: Iterator[str]) -> Iterator[str]:
        for rec in input_stream:
            if len(rec) <25:
                yield rec
            else:
                i = 0
                end_index = i + 25
                for i in  range(len(rec)):
                    yield rec[i:end_index]
                    i = end_index
                    end_index = len(rec) - i
