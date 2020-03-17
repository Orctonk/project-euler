from gcd import gcd

def flc(f1,f2):
    return (abs(f1-f2) < 0.0005)
    
def isDigCanc(nom,den):
    if nom % 10 == 0 and den % 10 == 0:
        return False

    truefrac = float(nom)/den

    nomstr = str(nom)
    denstr = str(den)

    for c in nomstr:
        if c in denstr:
            newnom = float(nomstr.replace(c,"",1))
            newden = float(denstr.replace(c,"",1))
            if newden != 0 and flc(truefrac,newnom/newden):
                return True

    return False
    
nom = 1
den = 1

for n in range(11,99):
    for d in range(n+1,100):
        if isDigCanc(n,d):
            nom = nom * n
            den = den * d

g = gcd(nom,den)

print(int(den/g))