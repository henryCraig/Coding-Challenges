#https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
import random

#TODO: add in multi arg functionality

def diceRoller(diceString):
    #print(2*int(diceString[0]))
    iterator = 0
    randList = []
    #for i number of Arguments repeat this loop
    for i in range(int(diceString[0])):
        randomNum = random.randint(1,int(diceString[2:]))
        print(randomNum)
        randList.append(randomNum)
        iterator += randomNum
        print(randList)

    #TODO: this is some kind of loop which will take the list and impart it onto this string

    return iterator
    print(randList)
    #print(iterator, ": ", )




diceRoller('4d8')
