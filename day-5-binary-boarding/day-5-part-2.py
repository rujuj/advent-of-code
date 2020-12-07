import math

file = open("day-5-binary-boarding/input", "r")
lines = file.readlines()

seatIDs = []
max = 0
for line in lines:
    lower_row = 0
    upper_row = 127
    lower_seat = 0
    upper_seat = 7
    row = 0
    for char in line[0:6]:
        if char == 'F':
            upper_row = math.floor((lower_row + upper_row) / 2)
        else:
            lower_row = math.ceil((lower_row + upper_row) / 2)
    if line[6] == 'B':
        lower_row = upper_row
        row = upper_row
    else:
        upper_row = lower_row
        row = lower_row
    for char in line[7:9]:
        if char == 'L':
            upper_seat = math.floor((lower_seat + upper_seat) / 2)
        else:
            lower_seat = math.ceil((lower_seat + upper_seat) / 2)
    if line[9] == 'R':
        seat = upper_seat
    else:
        seat = lower_seat
    seatID = row * 8 + seat
    seatIDs.append(seatID)

seatIDs.sort()

for i in range(1, len(seatIDs)- 1):
    if seatIDs[i] - seatIDs[i - 1] != 1:
        print(seatIDs[i] - 1)
        break

# attempt 1: 598 - too high 
# oops forgot to subtract 1 from my flagged seat - got it on the second try :) 