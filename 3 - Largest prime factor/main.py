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

res = 0
val = 600851475143
sqrt = math.ceil(math.sqrt(val))

for i in range(sqrt,1,-1):
    if(val % i == 0 and isPrime(i)):
        res = i
        break

print(res)