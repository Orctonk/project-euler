import math

def genFib():
    last = cur = 1
    yield 1
    yield 1
    while True:
        cur = last + cur
        last = cur - last
        yield cur

val = 10**999

for (i,f) in enumerate(genFib()):
    if (f / val) >= 1:
        print(i+1)
        break