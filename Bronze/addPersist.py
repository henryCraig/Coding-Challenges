#https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/
#The program uses the bonus challenge of never converting the int into a string

def addPersist(manipulable):
    print('originalNum:', manipulable)

    timesIter = 0
    while manipulable > 9:
        newNum = 0
        iterator = 1
        while iterator < manipulable:
            singleNum = (manipulable % (iterator*10) - manipulable % iterator) // iterator
            newNum += singleNum
            iterator *= 10

        manipulable = newNum
        timesIter += 1

    print('Additive Persistence: ', timesIter)
addPersist(13)
