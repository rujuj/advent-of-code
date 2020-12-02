file = open("day-2/input", "r")
lines = file.readlines()

valid_passwords = 0

for line in lines:
    components = line.split(" ")
    limits = components[0].split("-")
    letter = components[1][0]
    password = components[2]
    letter_counter = 0

    for pos in limits:
        if password[int(pos)-1] == letter:
            letter_counter += 1
    if letter_counter == 1:
        valid_passwords += 1

print(valid_passwords)