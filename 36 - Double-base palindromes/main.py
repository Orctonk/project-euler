def isPalindrome(val: str) -> bool:
    mid = int(len(val)/2)
    
    if(len(val) % 2 == 0):
        if(val[0:mid] in val[:mid-1:-1]):
            return True
    else:
        if(val[0:mid] in val[:mid:-1]):
            return True
    
    return False

def toBinary(val: int) -> str:
    return bin(val)[2:]

s = 0
for i in range(1000000):
    if isPalindrome(str(i)):
        b2 = toBinary(i)
        if isPalindrome(b2):
            s = s + i

print(s)