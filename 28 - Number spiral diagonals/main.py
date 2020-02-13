def calcSpiralLayer(val):
    return 16*val*val - 28*val + 16

res = 1
for i in range(2,502):
    res = res + calcSpiralLayer(i)

print(res)