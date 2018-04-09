https://www.reddit.com/r/dailyprogrammer/comments/82pt3h/20180307_challenge_353_intermediate/

targetList = [3,2,1,4]

#takes a list as an arg, flips the first 3 numbers in the playlist
#returns the list
def flipFunc(flippingList):
    print(flippingList)
    flippingList[0], flippingList[2] = flippingList[2], flippingList[0]
    print(flippingList)

flipFunc(targetList)



print(max(targetList)) #this is the largest number, not the the length


#if max(targetList) == targetList(len(targetList)):


print(targetList[len(targetList)-1])

print(targetList[-1])

print(targetList)
targetList = targetList[:-1]
print(targetList)




newList = []
for i in range(len(targetList)):
    print("Old List: " + str(targetList) + '\n New List: ' + str(newList))
    print("Max: " + str(max(targetList)))
    newList.append(targetList[-1])
    targetList = targetList[:-1]
