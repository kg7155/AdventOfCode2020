""" Day 6: Custom Customs """
# PART TWO

groups = []
group = []
with open('inputs/6.txt') as f:
    for line in f:
        if (line == '\n'):
            groups.append(' '.join(group))
            group = []
        else:
            group.append(line.strip())

sum = 0
for group in groups:
    answers = group.split(' ')
    s = set(answers[0])
    for answer in answers[1:]:
        s = s.intersection(answer)
    sum += len(s)
print(sum)