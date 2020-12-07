""" Day 6: Custom Customs """
# PART ONE

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
    s = group.replace(' ','')
    sum += len(set(s))
print(sum)