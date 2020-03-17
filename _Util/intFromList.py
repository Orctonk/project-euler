def intFromList(l: list) -> int:
    pot = len(l) - 1
    res = 0
    for i in l:
        res = res + i * 10**pot
        pot = pot - 1
    return res