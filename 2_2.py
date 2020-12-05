""" Day 2: Password Philosophy """
# PART TWO

#lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
with open('inputs/2.txt') as f:
    lines = f.readlines()

def isValid(pos1, pos2, letter, pw):
    sum = 0
    if (pw[pos1] == letter):
        sum += 1
    if (pw[pos2] == letter):
        sum += 1
    if (sum == 1):
        return True
    return False

valid_count = 0
for line in lines:
    s = line.strip().split(' ')
    positions = s[0].split('-')
    pos1 = int(positions[0]) - 1
    pos2 = int(positions[1]) - 1
    letter = s[1][0]
    pw = s[2]
    if (isValid(pos1, pos2, letter, pw)):
        valid_count += 1
print(valid_count)