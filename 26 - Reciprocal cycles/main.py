import math

def isPrime(val):
    if(val == 2):
        return True
    elif(val < 2):
        return False

    for i in range(2,math.ceil(math.sqrt(val))):
        if(val % i == 0):
            return False

    return True

def factorize(val):
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


def intDiv(numer,denom,depth):
    ans = []

    for i in range(depth):
        div = int(numer / denom)
        res = numer - div*denom

        ans =  ans + [div]
        
        if res == 0:
            break
        else:
            numer = res * 10
    
    return ans
    
def isRep(data,repstart,replen):
    for i in range(replen*3):
        idx = repstart+i
        if data[idx] != data[idx + replen]:
            return False
    return True

def recipCycleLen(val):
    factors = factorize(val)

    found = False
    for i in factors:
        if i != 2 and i != 5:
            found = True
            break

    if not found:
        return 0

    nums = intDiv(1,val,val * 4)

    for i in range(1,val*4):
        val = nums[i]
        idx = nums.index(val,0)
        while idx < i:
            replen = i - idx
            if isRep(nums,idx,replen):
                return replen
            idx = nums.index(val,idx+1)

    return 0

maxlen = 0
maxd = 0

for i in range(2,1000):
    curlen = recipCycleLen(i)
    if curlen > maxlen:
        maxlen = curlen
        maxd = i


print("{}: {}".format(maxd, maxlen))