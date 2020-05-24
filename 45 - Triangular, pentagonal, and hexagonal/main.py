import math

def genHn():
    n = 0
    tn = 0
    while True:
        tn += 4*n+1
        n = n+1
        yield tn

def isPentagonal(pn):
    n = (1 + math.sqrt(1+24*pn))/6
    return n.is_integer()

def isTriangular(tn):
    n = -(1/2) + math.sqrt(1/4 + 2*tn)
    return n.is_integer()

gen = genHn()

for hn in gen:
    if isPentagonal(hn) and isTriangular(hn) and hn > 40755:
        print(hn)
        break