import math

def intSplit(num):
    resList=[num]
    logterm = int(math.log10(num))

    for i in range(logterm,0,-1):
        tenpot = int(math.pow(10,i))
        resList.insert(logterm-i,int(resList[-1]/tenpot))
        resList[logterm-i+1] -= tenpot * int(resList[-1]/tenpot)
    return resList

def nextFib(digs1,digs2):
    mindigs = len(digs1)
    digs = []
    for i in range(1,mindigs+1):
        digs.insert(0, digs1[-i] + digs2[-i])

    if len(digs2) > mindigs:
        digs2 = digs2[::-1]
        for i in digs2[-1:mindigs-1:-1]:
            digs.insert(0,i)

    for i in range(len(digs)-1,0,-1):
        digs[i-1] += int(digs[i]/10)
        digs[i] -= 10*int(digs[i]/10)
        if(digs[i] > 9):
            print("oops")

    logterm = int(math.log10(digs[0]))

    digSplit = intSplit(digs[0])
    digs.remove(digs[0])
    for i in digSplit[::-1]:
        digs.insert(0,i)


    return digs

cur = [1]
prev = [1]

for i in range(10):
    next = nextFib(prev,cur)
    prev = cur
    cur = next
    print(cur)