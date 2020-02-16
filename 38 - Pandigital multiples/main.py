import math
from typing import List

def intSplit(num: int) -> List[int]:
    resList=[num]
    logterm = int(math.log10(num))

    for i in range(logterm,0,-1):
        tenpot = int(math.pow(10,i))
        resList.insert(logterm-i,int(resList[-1]/tenpot))
        resList[logterm-i+1] -= tenpot * int(resList[-1]/tenpot)
    return resList
    
def overlap(l1: list, l2: list) -> bool:
    for i in l1:
        if i in l2:
            return True

    return False

def hasDupes(l: list):
    for (num,i) in enumerate(l):
        if i in l[num+1:]:
            return True
    return False

def getIntFromSplit(l: List[int]) -> int:
    pot = len(l)-1

    s = 0
    for i in l:
        s = s + i * 10**pot
        pot -= 1

    return s

longest = 0

for i in range(1,10001):
    conc = intSplit(i)
    if not hasDupes(conc) and not 0 in conc:
        ok = True
        j = 2
        while len(conc) < 9 and ok:
            n = intSplit(i * j)
            if not hasDupes(n) and not overlap(n,conc) and not 0 in n:
                conc = conc + n
                j = j + 1
            else:
                ok = False

        if ok and len(conc) == 9:
            val = getIntFromSplit(conc)
            if val > longest:
                longest = val

print(longest)