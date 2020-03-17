from gcd import gcd

def lcm(a :int, b :int) -> int:
    if a == 0 and b == 0:
        return 0

    return int((a * b) / gcd(a,b))