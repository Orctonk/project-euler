def getMonthDays(month,year):
    if month in [4,6,9,11]:
        return 30
    elif month != 2:
        return 31
    else:
        if year % 4 == 0 and (not (year % 100 == 0 and year % 400 != 0)):
            return 29
        else:
            return 28

curWeekday = 0

count = 0

for year in range(1900,2001):
    for month in range(1,13):
        for day in range(1,getMonthDays(month,year) + 1):
            curWeekday = (curWeekday + 1) % 7
            if(year > 1900 and day == 1 and curWeekday == 6):
                count += 1

print(count)