def addOne(number):
    if type(number) == type(1):

        strList = ''
        for i in range(len(str(number))):
            newNum = str((int(str(number)[i])+1))
            strList += newNum

    print(strList)
addOne(998)
