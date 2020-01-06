import math

res = 0

a_res = 0
b_res = 0
c_res = 0

for a in range(350):
    for b in range(a+1,500):
        c = 1000 - a - b
        if(math.sqrt(a*a + b*b).is_integer() and a*a + b*b == c*c):
            a_res = a
            b_res = b
            c_res = c
            res = a*b*c
            break
    if(res != 0):
        break

print(res)