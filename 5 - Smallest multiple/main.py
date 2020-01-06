import math

def isPrime(val):
    if(val == 2):
        return True
    elif(val < 2):
        return False

    for i in range(2,math.ceil(math.sqrt(val))+1):
        if(val % i == 0):
            return False

    return True

def primeFactors(val):
    result = []
    while not isPrime(val):
        for i in range(1,math.ceil(math.sqrt(val))+1):
            if(val % i == 0 and isPrime(i)):          
                val = val / i
                result.append(i)
                break
    result.append(int(val))
    return result

factors = []
for i in range(2,20):
    tempfac = primeFactors(i)
    for j in range(0,len(tempfac)):
        if factors.count(tempfac[j]) < tempfac.count(tempfac[j]):
            factors.append(tempfac[j])

prod = 1

for i in range(0,len(factors)):
    prod *= factors[i]

print(prod)