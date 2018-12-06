def iBeforeE(checkWord):
    if 'cie' in checkWord:
        return False
    elif 'ei' in checkWord:
        index = checkWord.find('ei')
        if (checkWord[index-1]) == 'c':
            iBeforeE(checkWord[index+1:])
        else:
            return False

    return True
print(iBeforeE('societies'))
