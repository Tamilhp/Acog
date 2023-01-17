import time
from typing import Callable


def timer(func: Callable[[int], int]) -> Callable[[int], None]:
    start = time.time()
    print("I am timer")

    def wrapper(n: int):
        """This is the wrapper function"""
        print("I am wrapper")
        i = func(n)
        stop = time.time()
        print(stop - start)
        return i
    return wrapper


@timer
def factorial(n: int) -> int:
    """This is the real function"""
    print("I am factorial")
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    # print(f"I am returning {result}")


print(factorial(2))


