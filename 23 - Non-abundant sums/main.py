def sumDivs(num):
    count = 1
    highval = num

    i = 2

    while i < highval:

        divres = num / i

        if divres.is_integer():
            count += i
            if i != divres:
                count += int(divres)
            highval = divres

        i+=1

    return count

abnums = []

for i in range(1,28124):
    if sumDivs(i) > i:
        abnums.append(i)

absums = []

for i in range(len(abnums)):
    for n2 in abnums[i:]:
        if abnums[i] + n2 > 28124:
            break
        absums.append(abnums[i]+n2)

sum = 0
for i in range(1,28124):
    if not i in absums:
        sum += i

print(sum)
