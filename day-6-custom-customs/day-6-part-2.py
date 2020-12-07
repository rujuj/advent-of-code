file = open("day-6-custom-customs/input", "r")
groups = file.read().split("\n\n")

yes_count = 0
for group in groups:
    distinct_people = group.split("\n")
    yes_questions = set()
    
    if len(distinct_people) > 1:
        for char in distinct_people[0]:
            inGroup = True
            for people in distinct_people[1:]:
                if char not in people:
                    inGroup = False
                    if char in yes_questions:
                        yes_questions.remove(char)
                    break
            if inGroup:
                yes_questions.add(char)
    elif len(distinct_people) == 1:
        yes_questions = distinct_people[0]
    yes_count += len(yes_questions)

                
print(yes_count)

# attempt 1: 3291 - too high
# attempt 2: 3162 - too high
# attempt 3: 3096 - too low :/
# during testing, I keep getting 3086 but that's not possible hmmm - I guess I'm missing some letters 
# wasn't adding up the letters for groups in which there was only 1 member properly - used a lot of assert statements to help 
# attempt 4: success - 3103