#https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/

def upcChecker(upc):
    upc = list(str(upc))

    #Adds leading zeros
    while len(upc) < 11:
        upc.insert(0, '0')

    #sums the odd numbers in the list
    upcSum = 0
    for i in range(0, 11, 2):
        upcSum += int(upc[i])

    upcSum *= 3

    evenSum = 0
    for i in range(1, 11, 2):
        evenSum += int(upc[i])

    upcSum += evenSum

    upcSum %= 10

    if upcSum == 0:
        print("checkDigit: ", 0)
    else:
        print("CheckDigit: ", 10-upcSum)

upcChecker(4210000526)
