import itertools

def isSSD(num):
    primes = [2,3,5,7,11,13,17]
    for i in range(1,8):
        if int(num[i:i+3]) % primes[i-1] != 0:
            return False

    return True 

available = "0123456789"

s = 0
for perm in itertools.permutations(available):
    st = "".join(perm)
    if isSSD(st):
        s += int(st)

print(s)