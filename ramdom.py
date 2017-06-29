from random import randint

def level2(numlist):
    numSum = 0

    for num in numlist:
        if num % 3 == 0 or num %5 == 0:
            numSum +=num
    print(numSum)

randomlist = []
for x in range(100):
    randomnumber = randint(10,99)
    randomlist.append(randomnumber)

level2(randomlist)
