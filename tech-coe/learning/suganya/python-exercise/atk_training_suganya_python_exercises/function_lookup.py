from typing import Callable
from atk_training_suganya_python_exercises.atktraining_sugan_py1 import transform_uppercase, transform_remove_stopwords, transform_lowercase

#function_list:dict={"upper_case": transform_uppercase, "stop_words": transform_remove_stopwords, "lower_case": transform_lowercase}


class FunctionalLoader:
    def __init__(self, *function):
        self.function: str = function
        self.function_list: dict = {"upper_case": transform_uppercase, "stop_words": transform_remove_stopwords, "lower_case": transform_lowercase}

    def get_function(self, opt: str) -> Callable[[str], str]:
        return self.function_list[opt]


# def lookup(opt:str) -> Callable[[str], str]:
#     return function_list[opt]

