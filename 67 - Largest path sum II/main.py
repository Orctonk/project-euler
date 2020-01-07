def getData():
    file = open("p067_triangle.txt","rt")

    data = ""
    for row in file:
        data += row

    data = data.replace("\n"," ")

    return data.strip()

data = getData()

splitData = data.split(" ")

print(splitData)

maxPath = {0:0}
maxTot = 0

row = 0
for i in range(len(splitData)):
    maxPath[i] += int(splitData[i])

    rowSum = sum(range(row+1))
    if(i >= rowSum):
        row += 1
    
    if row + i + 1 < len(splitData):
        if row + i in maxPath:
            maxPath[row + i] = max([maxPath[row + i],maxPath[i]])
        else:
            maxPath[row + i] = maxPath[i]

        if row + i + 1 in maxPath:
            maxPath[row + i + 1] = max([maxPath[row + i + 1],maxPath[i]])
        else:
            maxPath[row + i + 1] = maxPath[i]

    if maxPath[i] > maxTot:
        maxTot = maxPath[i]

print(maxTot)