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
    decryptedString = ''


    def findColumn(char):
        columnLoc = int(char/6)
        columnarChunk = encryptKey[columnLoc*6:(columnLoc+1)*6]

        if char-columnLoc < (columnLoc+1)*6:
            columnLocation = char-leftMove+6
        else:
            columnLocation = char-leftMove

        print("Column: ", encryptKey[columnLocation])

        return columnLocation

    def findRow(columnLoc):
        rowLocation = columnLocation - (upMove*6)
        #and if we want ot to be positive we can do
        if rowLocation < 0:
            rowLocation = rowLocation+len(encryptKey)
        #but do we need to is the question?
        return rowLocation




    for char in range(len(encryptKey)):
        if encryptKey[char] == encryptedMessage[0]:
            print("Letter: ", encryptedMessage[0], " found at position: ", char, " of the encryptKey")


            #uses the markers location to find the vertical and horizontal movement
            leftMove = cipherAlpha.find(encryptKey[markerLocation])%6
            upMove = int(cipherAlpha.find(encryptKey[markerLocation])/6)



            columnLocation = findColumn(char)
            print("Column Location: ", columnLocation)
            print("upMove", upMove)

            rowLocation = findRow(columnLocation)
            print("rowLocation: ", encryptKey[rowLocation])
            print(encryptKey[-12])


            #at this point we still need to shift everything up
            #and then shift everything to the left
            #and then move the marker
            #and also append everything to a new list, which will be our output
            #we will use the decrypted string for this



            decryptedString += encryptKey[rowLocation]
            print("decryptedString: ", decryptedString)








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
