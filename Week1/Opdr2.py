a = 'een123zin45 6met-632meerdere+7777getallen'


def getNumbers(a):
    lastwasnumber = False
    tempnum = ""
    numberList = []
    for t in a:
        check = t.isdigit()
        if check:
            tempnum = (tempnum + t)
            lastwasnumber = True
        elif lastwasnumber:
            numberList.append(tempnum)
            tempnum = ""
            lastwasnumber = False

    return numberList


print(getNumbers(a))
