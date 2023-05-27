from functools import partial

def multiply(x, y):
        return x * y

dbl = partial(multiply, 9)
print(dbl(9))