import math

def loadWords(path: str) -> list:
    f = open(path,"r")
    return f.readline().replace('"',"").split(",")

def nFromTn(tn: int) -> float:
    return -0.5 + math.sqrt(1/4 + 2*tn)

def isWordTriangle(str: str) -> bool:
    tot = 0
    for char in str.lower():
        tot += ord(char) - 96
    return nFromTn(tot).is_integer()

count = 0
for word in loadWords("p042_words.txt"):
    if isWordTriangle(word):
        count += 1

print(count)