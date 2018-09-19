#https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/

def wordFunnel(baseWord, checkWord):
    checkList = list(checkWord)

    for i in range(len(baseWord)):
        baseList = list(baseWord)
        del baseList[i]
        if (baseList == checkList):
            return True
        elif(i == len(baseList)):
            return False

#print(wordFunnel('skiff', "ski"))
