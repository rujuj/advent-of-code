file = open("day-3-toboggan-trajectory/input", "r")
lines = file.readlines()

treecounter = 0
linelength = len(lines[0]) - 1
print(linelength)
xcounter = 0

for ycounter in range(len(lines)):
    # this line was very useful for validation
    # print(lines[ycounter] + " xcounter: " + str(xcounter) + " ycounter: " + str(ycounter) + " " + lines[ycounter][xcounter])
    if xcounter <= linelength:
        if lines[ycounter][xcounter] == '#':
            treecounter += 1
    if xcounter + 3 >= linelength:
        xcounter = (xcounter + 3) % linelength
    else:    
        xcounter += 3
    
print(treecounter)

# first attempt: 77 - wrong (had the wrong linelength and possibly faulty xcounter logic)
# second attempt: success :) 


