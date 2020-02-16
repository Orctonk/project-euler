import math

def factorial(x :int) -> int:
    if x == 0:
        return 1
    return x * factorial(x - 1)

def intSplit(num):
    resList=[num]
    logterm = int(math.log10(num))

    for i in range(logterm,0,-1):
        tenpot = int(math.pow(10,i))
        resList.insert(logterm-i,int(resList[-1]/tenpot))
        resList[logterm-i+1] -= tenpot * int(resList[-1]/tenpot)
    return resList

tot = 0
for i in range(10,255000):
    nums = intSplit(i)
    s = 0
    for n in nums:
        s = s + factorial(n)

    if s == i:
        tot = tot + i 

print(tot)
