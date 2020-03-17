def gcd(a: int,b:int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    r = a % b
    return gcd(b,r)