def loadNames():
    names = []

    f = open("p022_names.txt","rt")

    data = f.readline().replace('"',"").split(",")
    data.sort()

    return data

def charInt(char):
    chars = "abcdefghijklmnopqrstuvwxyz"

    return chars.index(char) + 1

def getNameScore(name):
    namesum = 0
    for c in name:
        namesum += charInt(c)

    return namesum

names = loadNames()

namesum = 0
for i in range(len(names)):
    namesum += (i+1) * getNameScore(names[i].lower())

print(namesum)