def getNumWord(num):
    onesWords = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teenWords = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen","seventeen","eighteen","nineteen"]
    tenWords = ["twenty","thirty","forty", "fifty","sixty","seventy","eighty", "ninety"]
    

    thousands = int(num / 1000)
    hundreds = int((num - thousands*1000) / 100)
    tens = int((num - thousands*1000 - hundreds*100) / 10)
    ones = int(num - thousands*1000 - hundreds*100 - tens*10)

    if thousands + hundreds + tens == 0:
        return onesWords[ones]
    
    elif thousands + hundreds == 0 and tens == 1:
        return teenWords[ones]

    elif thousands + hundreds == 0 and ones == 0:
        return tenWords[tens-2]

    elif thousands + hundreds == 0:
        word = getNumWord(tens * 10)
        if ones > 0:
            word += "-" + getNumWord(ones)
        return word

    word = ""

    if thousands > 0:
        word += getNumWord(thousands) + " thousand"

    if hundreds > 0:
        if len(word) != 0:
            word += " "
        word += getNumWord(hundreds) + " hundred"

    if tens + ones > 0:
        if len(word) != 0:
            word += " and "
        word += getNumWord(tens*10+ones)

    return word

def countLetters(word):
    count = 0
    for c in word:
        if c.isalpha():
            count += 1
    return count

sum = 0

for i in range(1,1001):
    sum += countLetters(getNumWord(i))

print(sum)