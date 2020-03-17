totsum = 0

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        res = a**5 + b**5 + c**5 + d**5 + e**5 + f**5
                        if res == a*100000 + b*10000 + c*1000 + d*100 + e*10 + f:
                            totsum = totsum + res

totsum = totsum - 1
print(totsum)