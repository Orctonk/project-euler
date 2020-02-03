import math

def isPrime(val):
    if(val == 2):
        return True
    elif(val < 2):
        return False

    for i in range(2,math.ceil(math.sqrt(val))):
        if(val % i == 0):
            return False

    return True

def getQuadLength(a,b):
    i = 0
    while(True):
        if not isPrime(i*i + a*i + b):
            return i - 1
        i = i+1

maxa = 0
maxb = 0
maxlen = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        curlen = getQuadLength(a,b)
        if curlen > maxlen:
            maxa = a
            maxb = b
            maxlen = curlen
            print("a={}, b={}, len={}".format(a,b,maxlen))
