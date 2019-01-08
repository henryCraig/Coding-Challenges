#https://www.reddit.com/r/dailyprogrammer/comments/8jvbzg/20180516_challenge_361_intermediate_elsiefour/

#The thing I want to remember building it this time around is that we are working with 0-35
#yes there are 36 characters, but the number starts at 0


def lc4(key, encryptedMessage):
    cipherAlpha = "#_23456789abcdefghijklmnopqrstuvwxyz"
    key = list(key)
    encryptedMessage = list(encryptedMessage)
    decryptedString = ''
    markerChar = key[0]
    markerLoc = 0

    for messageChar in range(len(encryptedMessage)):
        cipherLoc = key.index(encryptedMessage[messageChar])                    #finds the ciphertext characters location in the Key
        print("Cipher Loc: ", cipherLoc, ", Cipher Char: ", key[cipherLoc])


        print("markerLoc: ", markerLoc, "markerChar: ", markerChar)             #prints out the marker early so that we can verify its doing the up and left moves correctly


        cipherLeft = cipherAlpha.find(key[markerLoc])%6                         #Creating the left and up moves for finding the plaintext character
        cipherUp = int(cipherAlpha.find(key[markerLoc])/6)                      #These are created using the current marker location
        print("cipherLeft:",cipherLeft,"cipherUp",cipherUp)



        plainLoc = cipherLoc                                                    #setting the plaintext location to equal the ciphertext location
        if cipherLeft > cipherLoc % 6:                                          #so that we can perform operations on it
            plainLoc = plainLoc + 6 - cipherLeft
        else:
            plainLoc -= cipherLeft

        plainLoc -= cipherUp*6                                                  #finds the char within the column
        if plainLoc < 0:
            plainLoc += 36

        decryptedString += key[plainLoc]
        print("plainLoc:", plainLoc, "planLocChar:", key[plainLoc])




        #we set these up before sliding things around
        rightMarkerMove = cipherAlpha.find(key[cipherLoc])%6
        downMarkerMove = int(cipherAlpha.find(key[cipherLoc])/6)


        #start of the tracking for the cipher char
        cipherChar = key[cipherLoc]

        #(right-rotate on plaintext tile, down-rotate on ciphertext tile)
        columnLoc = int(plainLoc/6)                                             #Shifting the Row, and then the column in the KEY
        key[columnLoc*6:(columnLoc+1)*6] = [key[(columnLoc+1)*6-1]] + key[columnLoc*6:(columnLoc+1)*6-1]

        #2nd part of the cipherChar tracking
        cipherLoc = key.index(cipherChar)

        ciphCol = cipherLoc % 6
        for i in range(30, 0, -6):
            key[i+ciphCol], key[i-6+ciphCol] = key[i-6+ciphCol], key[i+ciphCol]


        #print(key)


        markerLoc = key.index(markerChar)                                       #finds the marker again, just in case it moved
        print("Marker Char: ", markerChar)

        #These are created above the shifiting functions
        print("rightMarkerMove: ", rightMarkerMove)
        print("downMarkerMove: ", downMarkerMove)




        #Final Thing: Time to move the marker itself
        if (markerLoc % 6) + rightMarkerMove > 5:
            markerLoc += rightMarkerMove
            markerLoc -= 6
        else:
            markerLoc += rightMarkerMove

        markerLoc += downMarkerMove*6
        if markerLoc > 35:
            markerLoc -= 36

        print("markerLoc after Move: ", markerLoc, "at Char: ", key[markerLoc])

        markerChar = key[markerLoc]


        print()

    print("Return String: ", decryptedString)

lc4("9mlpg_to2yxuzh4387dsajknf56bi#ecwrqv", "grrhkajlmd3c6xkw65m3dnwl65n9op6k_o59qeq")


"""
Key - #o2zqijbkcw8hudm94g5fnprxla7t6_yse3v
Message - b66rfjmlpmfh9vtzu53nwf5e7ixjnp
output - be_sure_to_drink_your_ovaltine

Key - s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b
Message - tk5j23tq94_gw9c#lhzs
output - aaaaaaaaaaaaaaaaaaaa

Key - 9mlpg_to2yxuzh4387dsajknf56bi#ecwrqv
Message - grrhkajlmd3c6xkw65m3dnwl65n9op6k_o59qeq
output - congratulations_youre_a_dailyprogrammer
"""
