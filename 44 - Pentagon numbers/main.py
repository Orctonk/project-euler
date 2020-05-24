import math

def genPn():
    n = 0
    pn = 0
    while True:
        pn += 3*n+1
        n = n+1
        yield pn

def isPentagonal(pn):
    n = (1 + math.sqrt(1+24*pn))/6
    return n.is_integer()

pnumgen = genPn()
pnums = [next(pnumgen)]
minPdiff = 0

count = 0
while minPdiff == 0:
    pnums.append(next(pnumgen))
    count = count + 1

    pk = pnums[count]
    
    for pj in pnums[-2:0:-1]:
        if isPentagonal(pk-pj) and isPentagonal(pk+pj):
            minPdiff = pk-pj


    
print(minPdiff)
    