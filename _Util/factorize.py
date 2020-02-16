import math
from typing import List

def factorize(val: int) -> List[int]:
    if(int(val) != val):
        return None
    if(val < 2):
        return None
    if(val == 2):
        return [val]
    
    found = False
    for i in range(2,math.floor(math.sqrt(val)) + 2):
        if(val % i == 0):
            found = True
            break
    
    if not found:
        return [int(val)]

    return factorize(i) + factorize(val / i)