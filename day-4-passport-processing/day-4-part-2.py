# this was so tedious, i did not have a good time

import re

def checkdates(currfield, field):
    if int(currfield) < ranges[field][0] or int(currfield) > ranges[field][1]:
        return False
    else:
        return True

def checkheight(currfield):
    if currfield[-2:] == 'cm':
        if int(currfield[:-2]) < ranges['cm'][0] or int(currfield[:-2]) > ranges['cm'][1]:
            return False
    elif currfield[-2:] == 'in':
        if int(currfield[:-2]) < ranges['in'][0] or int(currfield[:-2]) > ranges['in'][1]:
            return False
    else:
        return False

file = open("day-4-passport-processing/input", "r")
lines = file.read()

passports = lines.split("\n\n")

mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyecolours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
ranges = {'byr':[1920, 2002], 'iyr':[2010, 2020], 'eyr':[2020, 2030], 'cm':[150, 193], 'in':[59, 76]}
validpasses = 0

for passport in passports:
    valid = True
    keys = []
    passdict = {}
    pairs = re.split("\n| ", passport)

    for pair in pairs:
        splitpair = pair.split(":")
        if len(splitpair) == 2:
            key = splitpair[0]
            keys.append(key)
            passdict[key] = splitpair[1]

    for field in mandatory:
        if field not in passdict:
            valid = False
            break
        currfield = passdict.get(field)
        try:
            if field == 'byr' or field == 'iyr' or field == 'eyr':
                valid = checkdates(currfield, field)
                if valid == False:
                    break
            if field == 'hgt':
                valid = checkheight(currfield)
                if valid == False:
                    break
            if field == 'hcl':
                if currfield[0] == '#' and len(currfield) == 7:
                    valid = re.match("^[0-9a-f]*", currfield[-6:])
                    if valid == False:
                        break
                else:
                    valid = False
            if field == 'ecl' and (currfield not in eyecolours):
                valid = False
            if field == 'pid' and (len(currfield) != 9 or not int(currfield)):
                valid = False
        except:
            valid = False
        
    if valid:
        validpasses += 1

print(validpasses)

# first try: guessed 159 - but there some errors so it was more of a please let this work trial
# second try: guessed 139 - added a break in a line that shouldn't have affected anything but still wrong :'( 
# third try: added an additional break and modularized the code - success!