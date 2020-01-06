def countDivs(num):
    count = 2
    highval = num

    i = 2

    while i < highval:

        divres = num / i

        if divres.is_integer():
            count +=2
            highval = divres

        i+=1

    return count

nextInt = 2
triang = 1
while countDivs(triang) <= 500:
    triang += nextInt
    nextInt += 1

print(triang)