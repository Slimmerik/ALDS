import random

def fillListWith23RandomNumbersBetween1and360():
    a = []
    for i in range(0,22):
        i = random.randint(1,365)
        a.append(i)
    return a


def honderdkeer2verjaardagenhetzelfde():
    a = []
    dupliatesInList = 0
    for i in range(0,99):
        a.append(fillListWith23RandomNumbersBetween1and360())

    for list in a:
        dupliates = 0
        for valueOneInList in list:
            teller = 0
            for checkValue in list:
                if(checkValue == valueOneInList):
                    teller = teller +1
            if(teller > 1):
                dupliates = dupliates +1
        if(dupliates > 0):
            dupliatesInList = dupliatesInList +1

    #print(dupliatesInList)
    return dupliatesInList

print (honderdkeer2verjaardagenhetzelfde(),"%")