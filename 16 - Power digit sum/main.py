import math

def mult2(digs):
    for i in range(len(digs)):
        digs[i] *= 2

    for i in range(len(digs)-1,0,-1):
        digs[i-1] += int(digs[i]/10)
        digs[i] -= 10*int(digs[i]/10)

    logterm = int(math.log10(digs[0]))

    for i in range(logterm,0,-1):
        tenpot = int(math.pow(10,i))
        digs.insert(logterm-i,int(digs[logterm-i]/tenpot))
        digs[logterm-i+1] -= tenpot * int(digs[i]/tenpot)

    return digs

digs = [2]
for i in range(999):
    mult2(digs)

digsum = sum(digs)

print(digsum)