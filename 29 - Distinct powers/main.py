tlim = 100

pows = []
for a in range(2,tlim+1):
    for b in range(2,tlim+1):
        res = pow(a,b)
        if not res in pows:
            pows.append(res)

print(len(pows))