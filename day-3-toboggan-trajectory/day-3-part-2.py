file = open("day-3-toboggan-trajectory/input", "r")
lines = file.readlines()

treecounter = 0
linelength = len(lines[0]) - 1
xcounter = 0

slopes = [[1, 3, 0], [3, 1, 0], [5, 1, 0], [7, 1, 0], [1, 2, 0]]
treecounter = 1

for slope in slopes:
    for ycounter in range(len(lines))[::slope[1]]:
        # this line was very useful for validation
        # print(lines[ycounter] + " xcounter: " + str(xcounter) + " ycounter: " + str(ycounter) + " " + lines[ycounter][xcounter])
        if xcounter <= linelength:
            if lines[ycounter][xcounter] == '#':
                slope[2] += 1
        if xcounter + slope[0] >= linelength:
            xcounter = (xcounter + slope[0]) % linelength
        else:    
            xcounter += slope[0]
    treecounter *= slope[2]
print(treecounter)