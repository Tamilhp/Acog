from decor import timing
#Problem 2
@timing
def func1(s):
    print(s.replace("T", "U"))

@timing
def func2(s):
    joint = []
    for x in s:
        joint.append(x) if x is not "T" else joint.append("U")
    print("".join(joint))

@timing
def func3(s):
    print("U".join(s.split("T")))

__all__ = [func1, func2, func3]