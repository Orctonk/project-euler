import math

def isPrime(val : int) -> bool:
    if(val == 2):
        return True
    elif(val < 2):
        return False

    for i in range(2,math.ceil(math.sqrt(val))):
        if(val % i == 0):
            return False

    return True