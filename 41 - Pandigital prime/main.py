import itertools
import math

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

def intFromList(l: list) -> int:
    pot = len(l) - 1
    res = 0
    for i in l:
        res = res + i * 10**pot
        pot = pot - 1
    return res

largest = 0
available = [1,2,3,4]
for perm in itertools.permutations(available):
    i = intFromList(perm)
    if isPrime(i) and i > largest:
        largest = i

available = [1,2,3,4,5,6,7]
for perm in itertools.permutations(available):
    i = intFromList(perm)
    if isPrime(i) and i > largest:
        largest = i

print(largest)

