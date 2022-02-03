import math;

primeDict = {}

for i in range(2,10000):
    if not i in primeDict:
        primeDict[i] = True
    for j in range(i+i,10000,i):
        primeDict[j] = False

for i in range(1000,10000):
    o = i%10
    t = int((i%100)/10)
    h = int((i%1000)/100)
    th = int(i/1000)
    l = [th,h,t,o]
    print(l)