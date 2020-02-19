def getInterval(num: int) -> (int,int,int):
    threshNext = 0
    threshPot = 0
    while threshNext < num:
        threshNext += (threshPot+1) * 9 * 10 ** threshPot
        threshPot += 1

    threshPot -= 1
    thresh = threshNext  - (threshPot+1) * 9 * 10 ** threshPot

    return (threshPot,thresh)

def getDn(n: int) -> int:
    (pot,t) = getInterval(n)

    reduced = (n - t) - 1
    nPartOf = 10 ** pot + int(reduced/(pot+1))
    redPos = reduced % (pot + 1)

    return int(str(nPartOf)[redPos])
        
print(getDn(1) * getDn(10) * getDn(100) * getDn(1000) * getDn(10000) * getDn(100000) * getDn(1000000)) 