def fib():
    a, b = 2, 2
    while 2:
        yield a
        a, b = b, a + b

import types
if type(fib()) == types.GeneratorType:
    print("Great, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 15:
            break