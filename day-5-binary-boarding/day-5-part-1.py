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
        print(lower_seat, " to ", upper_seat)
    if line[9] == 'R':
        seat = upper_seat
    else:
        seat = lower_seat
    seatID = row * 8 + seat
    seatIDs.append((seatID, row, seat, line))

    if seatID > max:
        max = seatID
    print(max, " ", seatID)

print(seatIDs)
print(max)

# first try: 519 - too low
# second try: 807 - too high 
# third try: 803 - too high
# okay this was dumb as hell - was doing line[7:8] because I genuinely thought it was right and it was actually wrong because I don't know how python arrays work apparently
# got it on the 4th try (in fairness, I was very close in try 2 and 3)