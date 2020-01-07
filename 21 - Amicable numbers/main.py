def sumDivs(num):
    count = 1
    highval = num

    i = 2

    while i < highval:

        divres = num / i

        if divres.is_integer():
            count += i + int(divres)
            highval = divres

        i+=1

    return count

amSum = 0

for i in range(10000):
    divSum = sumDivs(i)

    if sumDivs(divSum) == i and i != divSum:
        amSum += i

print(amSum)
