import math
from typing import List

def factorize(val):
    if(int(val) != val):
        return None
    if(val < 2):
        return None
    if(val == 2):
        return {val}
    
    found = False
    for i in range(2,math.floor(math.sqrt(val)) + 2):
        if(val % i == 0):
            found = True
            break
    
    if not found:
        return {int(val)}

    return factorize(i).union(factorize(val / i))

cur_con = 0
n = 3
factorizations = [
    {},
    {},
    {},
    {}
]

while True:
    fac = factorize(n)
    if len(fac) != 4:
        cur_con = 0
    else:
        cur_con += 1
        

    n += 1
