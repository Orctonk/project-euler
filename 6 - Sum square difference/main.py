sumsqr = 0

sqrsum = 0

for i in range(1,101):
    sqrsum += i
    sumsqr += i*i

print(sqrsum * sqrsum - sumsqr)