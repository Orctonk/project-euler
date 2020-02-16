import math

def isRight(a: int, b: int) -> int:
    c = math.sqrt(a**2+b**2)
    if not c.is_integer():
        return None
    return int(c)

numSols = {}
maxSols = (0,0)
for a in range(1,334):
    for b in range(a,500):
        c = isRight(a,b)
        if c != None:
            p = a + b + c
            if p in numSols:
                numSols[p] += 1
            else:
                numSols[p] = 1

            if numSols[p] > maxSols[1]:
                maxSols = (p, numSols[p])

print(maxSols)

            