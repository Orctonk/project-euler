def intFromList(l):
    pot = len(l) - 1
    res = 0
    for i in l:
        res = res + i * 10**pot
        pot = pot - 1
    return res

def getProdsforChosen(prods, chosen, available):
    for i in range(1,len(chosen)):
        fac1 = intFromList(chosen[:i])
        fac2 = intFromList(chosen[i:])
        res = fac1 * fac2
        ress = str(res)
        ok = True
        for c in ress:
            if ress.count(c) > 1 or not (int(c) in available):
                ok = False
                break
        if ok and not (res in prods):
            print("{} * {} = {}".format(fac1,fac2,res))
            prods.append(res)
    return prods
        

def getProds(prods, chosen, available):
    if len(chosen) == 5:
        prods = getProdsforChosen(prods, chosen,available)

    for i in available:
        prods = getProds(prods,chosen + [i],list(filter(lambda x: x != i,available))) 

    return prods

available = [1,2,3,4,5,6,7,8,9]
prods = getProds([],[],available)

print(sum(prods))