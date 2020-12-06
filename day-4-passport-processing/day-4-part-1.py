import re

file = open("day-4-passport-processing/input", "r")
lines = file.read()

passports = lines.split("\n\n")

mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validpasses = 0

for passport in passports:
    pairs = re.split("\n| ", passport)
    keys = []

    for pair in pairs:
        key = pair.split(":")[0]
        keys.append(key)

    valid = True
    for field in mandatory:
        if field not in keys:
            valid = False
    if valid:
        validpasses += 1

print(validpasses)

# first attempt: tried 89 - incorrect
# second attempt: success - used the re package instead of just trying to split by both space and newline together 








