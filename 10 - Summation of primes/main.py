primes = [2]

curval = 3
while(primes[-1] < 2000000):
    prime = True
    for i in primes:
        if i * i > curval:
            break
        if curval % i == 0:
            prime = False
            break
    if prime:
        primes.append(curval)
    curval += 2

sum = 0

for i in primes[:-1]:
    sum += i

print(sum)