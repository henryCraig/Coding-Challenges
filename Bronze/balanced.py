#https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

def balanced(string):
    if len(string) > 0:
        charDict = {}

        for i in string:
            if i in charDict:
                charDict[i] += 1
            else:
                charDict[i] = 1

        importantNum = charDict[string[0]]
        for i in charDict:
            if importantNum != charDict[i]:
                print(string)
                return False

    print(string)
    return True

print(balanced("fdedfdeffeddefeeeefddf"))
