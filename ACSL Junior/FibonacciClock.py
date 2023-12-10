def findTime(c1, c2, c3, c4, c5):
    hour = 0
    minute = 0
    hour += addHour(c1, 1)
    hour += addHour(c2, 1)
    hour += addHour(c3, 2)
    hour += addHour(c4, 3)
    hour += addHour(c5, 5)
    minute += addMinute(c1, 1)
    minute += addMinute(c2, 1)
    minute += addMinute(c3, 2)
    minute += addMinute(c4, 3)
    minute += addMinute(c5, 5)
    minute *= 5
    strHour = str(hour)
    strMinute = str(minute)
    if hour < 10:
        strHour = "0" + strHour
    if minute < 10:
        strMinute = "0" + strMinute
    return strHour + ":" + strMinute


def addHour(color, delta):
    if color == 'R' or color == 'B':
        return delta
    return 0

def addMinute(color, delta):
    if color == 'G' or color == 'B':
        return delta
    return 0

input = [['R', 'W', 'G', 'B', 'G'],
         ['W', 'B', 'B', 'G', 'R'],
         ['B', 'G', 'B', 'B', 'R'],
         ['W', 'W', 'W', 'B', 'B'],
         ['W', 'R', 'G', 'G', 'G'],
         ['G', 'R', 'W', 'B', 'B'],
         ['R', 'B', 'B', 'W', 'G'],
         ['W', 'W', 'W', 'W', 'W'],
         ['B', 'W', 'W', 'G', 'R'],
         ['W', 'B', 'B', 'B', 'B']]

output = ["04:50", "08:30", "11:35", "08:40", "01:50", "09:45", "04:40", "00:00", "06:20", "11:55"]

for i in range(10):
    result = findTime(input[i][0], input[i][1], input[i][2], input[i][3], input[i][4])
    if output[i] == result:
        print(result)
    else:
        print("Test Case {}: Failed!".format(i))



