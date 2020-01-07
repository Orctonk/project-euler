def nFactorial(n):
    if n == 0:
        return 1
    return n * nFactorial(n-1)

def findNthPerm(digs,n):
    digs.sort()

    if n == 0:
        return digs

    permsPerDig = nFactorial(len(digs) - 1)

    if n >= permsPerDig * len(digs):
        digs.reverse()
        return digs
    
    firstDig = int(n / permsPerDig)

    temp = digs[0]
    digs[0] = digs[firstDig]
    digs[firstDig] = temp

    digs = [digs[0]] + findNthPerm(digs[1:],n - firstDig * permsPerDig)

    return digs

digs = [0,9,8,7,6,5,4,3,2,1]

digs = findNthPerm(digs,999999)

print(digs)

# 2, 0 -> 0 1->1 2->2