file = open("day-6-custom-customs/input", "r")
groups = file.read().split("\n\n")

yes_count = 0

for group in groups:
    # distinct_people = group.split("\n")
    group_yes = ""

    # for person in distinct_people:
    for char in group:
        if char == '\n' or char == ' ':
            continue
        elif char not in group_yes:
            group_yes += char
    yes_count += len(group_yes)

print(yes_count)

# yas I got this one on the first try, no debugging required :relieved:
# could also make group_yes a set