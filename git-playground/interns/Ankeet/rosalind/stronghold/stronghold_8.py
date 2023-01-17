from decor import timing
#Problem 4
@timing
def func1(n,k):
    if n is 0 or n is 1:
        return 1
    else: 
        return (func1(n-1, k) + k * func1(n-2, k))

@timing
def func2(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b

__all__ = [func1, func2]
