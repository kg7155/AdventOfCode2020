""" Day 2: Password Philosophy """
# PART ONE

#lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
with open('inputs/2.txt') as f:
    lines = f.readlines()

def isValid(min, max, letter, pw):
    n = pw.count(letter)
    if (n >= min and n <= max):
        return True
    return False

valid_count = 0
for line in lines:
    s = line.strip().split(' ')
    minmax = s[0].split('-')
    min = int(minmax[0])
    max = int(minmax[1])
    letter = s[1][0]
    pw = s[2]
    if (isValid(min, max, letter, pw)):
        valid_count += 1
print(valid_count)