primes = [2]

curval = 3
while(len(primes) < 10001):
    prime = True
    for i in primes:
        if curval % i == 0:
            prime = False
            break
    if prime:
        primes.append(curval)
    curval += 2

print(primes[10000])