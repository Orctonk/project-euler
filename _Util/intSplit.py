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