#https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

def talkingClock(theTime):
    hourList = ['twelve','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    onesList = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    tensList = ['o\'', 'ten', 'twenty', 'thirty', 'forty', 'fifty']

    hour = int(theTime[:2])
    tensMinute = int(theTime[3:4])
    onesMinute = int(theTime[4:])
    if hour > 12:
        hour = hour-12
        meridian = 'pm'
    else:
        meridian = 'am'


    verbHour = hourList[hour]
    verbTens = tensList[tensMinute]
    verbOnes = onesList[onesMinute]


    print(f"It is {verbHour} {verbTens} {verbOnes} {meridian}")
talkingClock("04:36")
