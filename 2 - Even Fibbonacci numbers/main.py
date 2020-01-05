first = 1
second = 2

sum = 2

while(second < 4000000):
    second = first + second
    first = second - first

    if second % 2 == 0:
        sum += second

print(sum)