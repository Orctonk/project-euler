def isPalindrome(val):
    valString = str(val)

    mid = int(len(valString)/2)
    
    if(len(valString) % 2 == 0):
        if(valString[0:mid] in valString[:mid-1:-1]):
            return True
    else:
        if(valString[0:mid] in valString[:mid:-1]):
            return True
    
    return False

res = 0
for x in range(999):
    for y in range(999):
        calc = x*y
        if isPalindrome(calc) and calc > res:
            res = calc

print(res)
