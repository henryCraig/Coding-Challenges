#https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
import random

def diceRoller(diceString):
    iterator = 0
    randList = []
    dLoc = diceString.find("d")


    for i in range(int(diceString[:dLoc])):
        randomNum = random.randint(1,int(diceString[dLoc+1:]))
        randList.append(randomNum)
        iterator += randomNum

    #TODO: this is some kind of loop which will take the list and impart it onto this string

    print(iterator, ":", str(randList))
    return iterator


diceRoller('10d18')
