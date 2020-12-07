file = open("day-1-report-repair/input", "r")
lines = file.readlines()
found = False

lines = list(map(int, lines))

for i in lines:
    for j in lines[1:]:
        if (i + j) == 2020:
            found = True
            print (i * j)
            break
    if found == True:
        break
file.close()