def nextCollatz(num):
    if num % 2 == 0:
        return num/2
    else:
        return num * 3 + 1

def lenCollatz(start,mem):
    if start == 1:
        return 1
    
    nextC = nextCollatz(start)

    if nextC in mem:
        mem[start] = mem[nextC] + 1
    else:
        mem[start] = lenCollatz(nextC,mem) + 1
    
    return mem[start]

mem = {}

largestCount = 1
for i in range(2,1000000):
    length = lenCollatz(i,mem)
    if length > lenCollatz(largestCount,mem):
        largestCount = i

print(largestCount)