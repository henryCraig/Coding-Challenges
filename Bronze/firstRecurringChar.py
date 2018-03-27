#https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

decipherableString = input("Input string to decipher please: ")

for i in range(len(decipherableString)):
    for j in range(i+1):
        if decipherableString[i] == decipherableString[j] and i != j:
            print(decipherableString[i] + " in location " + str(j+1))
            print(decipherableString[i] + " in location " + str(i+1))
            break
    if decipherableString[i] == decipherableString[j] and i != j:
        break
