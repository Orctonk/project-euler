import math

def intSplit(num):
    resList=[num]
    logterm = int(math.log10(num))

    for i in range(logterm,0,-1):
        tenpot = int(math.pow(10,i))
        resList.insert(logterm-i,int(resList[-1]/tenpot))
        resList[logterm-i+1] -= tenpot * int(resList[-1]/tenpot)
    return resList

def multn(digs,n):
    for i in range(len(digs)):
        digs[i] *= n

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

digs = [1]

for i in range(1,101):
    multn(digs,i)

print(digs)
digsum = sum(digs)

print(digsum)