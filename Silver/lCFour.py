#https://www.reddit.com/r/dailyprogrammer/comments/8jvbzg/20180516_challenge_361_intermediate_elsiefour/

"""
Decryption is the same, but it (obviously) starts from the ciphertext character,
and the plaintext is computed by moving along the negated vector (left and up)
of the tile under the marker. Rotation and marker movement remains the same
(right-rotate on plaintext tile, down-rotate on ciphertext tile).
"""


"""
be_sure_to_drink_your_ovaltine
['#', 'o', '2', 'z', 'q', 'i',
'j', 'b', 'k', 'c', 'w', '8',
'h', 'u', 'd', 'm', '9', '4',
'g', '5', 'f', 'n', 'p', 'r',
'x', 'l', 'a', '7', 't', '6',
'_', 'y', 's', 'e', '3', 'v']
"""
#t is at the 29th location on the cipherAlphabet



"""
aaaaaaaaaaaaaaaaaaaa
 ['s', '2', 'f', 'e', 'r', 'w',
 '_', 'n', 'x', '3', '4', '6',
 't', 'y', '5', 'o', 'd', 'i',
 'u', 'p', 'q', '#', 'l', 'm',
 'z', '8', 'a', 'j', 'h', 'g',
 'c', 'v', 'k', '7', '9', 'b']
"""
#but # is on the 0th element of the cipher alphabet so it MUST return a zero for me


#I think this needs cleaned up


def lCFour(encryptKey, encryptedMessage):
    cipherAlpha = "#_23456789abcdefghijklmnopqrstuvwxyz"
    markerLocation = 0
    encryptKey = list(encryptKey)                                               # #o2zqijbkcw8hudm94g5fnprxla7t6_yse3v
    encryptedMessage = list(encryptedMessage)                                   # b66rfjmlpmfh9vtzu53nwf5e7ixjnp
    decryptedString = ''


    #print(f"encrpytKey: {encryptKey}")

    for messageChar in range(1):
        indexLocation = encryptKey.index(encryptedMessage[messageChar])
        print("Letter: ", encryptedMessage[messageChar], " found at position: ", indexLocation, " of the encryptKey")


        print("EncryptKey at Location: ", markerLocation)
        print("Location in the chipher alphabet: ", cipherAlpha.find(encryptKey[markerLocation]))

        #then we use that that characters location to give ourselves the horizontal and vertical movements
        leftMove = cipherAlpha.find(encryptKey[markerLocation])%6
        print(f'leftMove: {leftMove}')

        #Now we want to print out the letter a
        upMove = int(cipherAlpha.find(encryptKey[markerLocation])/6)
        print(f'upMove: {upMove}')


        #finds the character within the row - does the left move
        decryptLocation = indexLocation
        if leftMove > indexLocation % 6:
            decryptLocation = decryptLocation + 6 - leftMove
        else:
            decryptLocation -= leftMove


        #finds the char within the column
        decryptLocation -= upMove*6


        #we could just say, if decryptLocation negative, add 36
        if decryptLocation < 0:
            decryptLocation += 36

        print("decryptLocation: ", decryptLocation)
        print("Index Location: ", indexLocation)
        print("Char at decryptLocation: ", encryptKey[decryptLocation])

        #adds char found to the decryptedString
        decryptedString += encryptKey[decryptLocation]


        #It Works!!!! This shifts the plaintext char's ('a') row to the right!
        #I still think it could possibly be cleaned up in the future maybe, but that's something I will look into later
        columnLoc = int(decryptLocation/6)
        encryptKey[columnLoc*6:(columnLoc+1)*6] = [encryptKey[(columnLoc+1)*6-1]] + encryptKey[columnLoc*6:(columnLoc+1)*6-1]
        print(encryptKey[columnLoc*6:(columnLoc+1)*6])


        #and down rotate on the ciphertext tile


        """
        columnLoc = int(indexLocation/6)


        #This shifts an entire row to the left
        #And fixed the issue where it was adding an extra char!
        encryptKey[columnLoc*6:(columnLoc+1)*6] = [encryptKey[(columnLoc+1)*6-1]] + encryptKey[columnLoc*6:(columnLoc+1)*6-1]
        print(encryptKey[columnLoc*6:(columnLoc+1)*6])

        #print(f"encrpytKey: {encryptKey}")


        #after this we can print out the new encryptKey, and then put it into a grid, to determine if its working or not
        tempChar = encryptKey[columnLoc]
        #print(f"Temp: {tempChar}")

        for letter in range(6):
            encryptKey[columnLoc-(letter*6)] = encryptKey[columnLoc-(letter*6+6)]

        encryptKey[columnLoc+6] = tempChar

        #print(f"encrpytKey: {encryptKey}")



        #so at this point we need to move the marker
        #so now we need to move the marker 4 right and 1 down?

        #or maybe we have to reverse it for the decryption
        #so a for reverse, or char 4 for regular


        #we could get location 30 by reversing 1, and going down 4
        #we just need to formalize that procedure and have it do that every time
        #whatever happens we can create a way for it to go up or down, or left and right







        #This moves the markers column
        if markerLocation - 1 < 0:
            markerLocation += 5
        else:
            markerLocation -= 1

        print(f"Marker Location: {markerLocation}")
        #This moves the markers row
        #so we want to use minus so we dont get an index error


        markerLocation = 30
        print(f"First Marker Location: {markerLocation}")
        """


    print("decryptedString: ", decryptedString)



lCFour("s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b", 'tk5j23tq94_gw9c#lhzs')
#this should output "aaaaaaaaaaaaaaaaaa" like that


"""
Key - #o2zqijbkcw8hudm94g5fnprxla7t6_yse3v
Message - b66rfjmlpmfh9vtzu53nwf5e7ixjnp
output - be_sure_to_drink_your_ovaltine
"""

"""
Key - s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b
Message - tk5j23tq94_gw9c#lhzs
output - aaaaaaaaaaaaaaaaaaaa
"""
