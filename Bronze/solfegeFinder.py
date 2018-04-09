#https://www.reddit.com/r/dailyprogrammer/comments/7hhyin/20171204_challenge_343_easy_major_scales/

def note(chosenScale, chosenSolfege):
    chromaticScale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", ] #12 in total
    solfegeDict = {"Do": 0, "Re": 2, "Mi": 4, "Fa": 5, "So": 7, "La": 9, "Ti": 11}

    #major scales are comprised of seven notes
    majorScaleList = [] # empty list, created once scale chosen



    #finds the start of the major scale
    for i in range(len(chromaticScale)):
        if chosenScale == chromaticScale[i]:
            #print("starts at list number: " + str(i+1))
            break

    #creates a major scale out of the chromatic scale
    for g in range(7):
        if i+g >= len(chromaticScale):
            #wraps around the list if necessary
            majorScaleList.append(chromaticScale[i+g-len(chromaticScale)])
        else:
            majorScaleList.append(chromaticScale[i+g])

    #wraps around the major scale
    if solfegeDict[chosenSolfege] > 7:
        returnedNote = majorScaleList[0 + solfegeDict[chosenSolfege] -7]
    else:
        returnNote = majorScaleList[0 + solfegeDict[chosenSolfege]]


    #print(majorScaleList)
    print("Chosen Scale: " + chosenScale)
    print("Chosen Solfege: " + chosenSolfege)
    print("Returned Note: " + returnedNote)

note("D#", "La")
