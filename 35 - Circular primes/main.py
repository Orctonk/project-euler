import math

def shift(num: int, steps: int) -> int:
    snum = str(num)
    return int(snum[steps:] + snum[0:steps])

def isPrime(val : int) -> bool:
    if val == 2:
        return True
    elif val < 2:
        return False

    for i in range(2,math.ceil(math.sqrt(val))+1):
        if(val % i == 0):
            return False

    return True

def isCircularPrime(num: int) -> bool:
    if not isPrime(num):
        return False

    shifted = shift(num,1)
    steps = 2
    while shifted != num:
        if not isPrime(shifted):
            return False
        shifted = shift(num,steps)
        steps = steps + 1
    return True

count = 1

for i in range(3,1000000,2):
    if isCircularPrime(i):
        print(i)
        count = count + 1

print(count)