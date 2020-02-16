import math

def primeGen(lim: int):
    a = [True] * lim
    a[0] = a[1] = False

    for (i,isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i,lim,i):
                a[n] = False
    
def isPrime(val : int) -> bool:
    if val == 2:
        return True
    elif val < 2:
        return False
    if val % 2 == 0:
        return False

    for i in range(3,math.ceil(math.sqrt(val))+1,2):
        if(val % i == 0):
            return False

    return True

def isTruncatable(num: int) -> bool:
    strnum = str(num)
    l = len(strnum)

    if l == 1:
        return False

    for i in range(1,l):
        if not isPrime(int(strnum[i:])) or not isPrime(int(strnum[:-i])):
            return False

    return True

count = 0
s = 0

for p in primeGen(1000000):
    if isTruncatable(p):
        count = count + 1
        s = s + p
        if count == 12:
            break

print(s)
