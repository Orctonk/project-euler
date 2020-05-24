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

def squareExists(num, p):
    return math.sqrt((num-p)/2).is_integer()

n = 3
while True:
    for i in range(math.ceil(math.sqrt(n))):
        if isPrime(n - (i**2) * 2):
            break 
    else:
        print(n)
        break
    n += 2
