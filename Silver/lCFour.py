#https://www.reddit.com/r/dailyprogrammer/comments/8jvbzg/20180516_challenge_361_intermediate_elsiefour/


"""
So for decryption

We still start at the top left of the "cube-matrix"
Then we find the ciphertext char in this matrix
"""


"""
#swapping two items in a list , list size is 6 for minimum practice Size
pracList = [0,1,2,3,4,5]
print(pracList)
pracList[0], pracList[5] = pracList[5], pracList[0]
#inserts this in the second place, 0,1 - at this 1
pracList.insert(2, 29)
del pracList[2]


print(pracList)
"""





def lCFour(encryptKey, encryptedMessage):
    cipherAlpha = "#_23456789abcdefghijklmnopqrstuvwxyz"
    markerLocation = 0
    encryptKey = list(encryptKey)
    encryptedMessage = list(encryptedMessage)



    for i in range(len(encryptKey)):
        if encryptKey[i] == encryptedMessage[0]:
            print("Letter: ", encryptedMessage[0], " found at position: ", i, " of the encryptKey")
            print("Marker Location: ", encryptKey[markerLocation])
            print("Where the marker letter is in the alphabet: ", cipherAlpha.find(encryptKey[markerLocation]))



            #uses the markers location to find the vertical and horizontal movement
            leftMove = cipherAlpha.find(encryptKey[markerLocation])%6
            upMove = int(cipherAlpha.find(encryptKey[markerLocation])/6)
            print("Modulo: ", leftMove)   #horizontal - for decryption going Left
            print("Rounded Division: ", upMove)  #vertical - for decryption going Right


            columnLoc = int(i/6)
            columnarChunk = encryptKey[columnLoc*6:(columnLoc+1)*6]

            #going to try to print out the '5'
            if i-columnLoc < (columnLoc+1)*6:
                columnLocation = i-leftMove+6
                print("encryptKey: ", encryptKey[columnLocation])
            else:
                columnLocation = i-leftMove
                print("encryptKey: ", encryptKey[columnLocation])



            #so now we take the column location and use it to print out from the list, this will also need to wraparound
            print(columnLocation)

            print(encryptKey[columnLocation])
            rowLocation = columnLocation - (upMove*6)
            print(encryptKey[rowLocation])


            #if columnLocation - (upMove*6) < 0:



"""
s 2 f e r w
_ n x 3 4 6
t y 5 o d i
u p q # l m
z 8 a j h g
c v k 7 9 b
"""


lCFour("s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b", 'tk5j23tq94_gw9c#lhzs')
#this should output "aaaaaaaaaaaaaaaaaa" like that
