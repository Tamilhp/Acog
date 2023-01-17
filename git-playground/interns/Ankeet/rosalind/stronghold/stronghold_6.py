from decor import timing
#Problem 6
@timing
def func1(s):
    strings = s.split()
    s1 = strings[0].strip()
    s2 = strings[1].strip()
    print(sum(s1[i] != s2[i] for i in range(len(s1))))

@timing
def func2(s):
    import operator
    strings = s.split()
    s1 = strings[0].strip()
    s2 = strings[1].strip()
    print(sum(map(operator.ne, s1, s2)))

@timing
def func3(s):
    strings = s.split()
    s1 = strings[0].strip()
    s2 = strings[1].strip()
    print(sum(a != b for a, b in zip(s1, s2)))

__all__ = [func1, func2, func3]