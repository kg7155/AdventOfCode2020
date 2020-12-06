""" Day 4: Passport Processing """
import re

def has_required(pp):
    for field in required:
        if (field not in pp):
            return False
    return True

def is_valid(pp):
    x = 0
    fields = pp.split(' ')

    for field in fields:
        field_s = field.split(':')
        if (field_s[0] == 'ecl'):
            eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if (field_s[1] not in eye_colours):
                return False
        elif (field_s[0] == 'pid'):
            if (not field_s[1].isnumeric() or len(field_s[1]) != 9):
                return False
        elif (field_s[0] == 'eyr'):
            num = int(field_s[1])
            if (num < 2020 or num > 2030):
                return False
        elif (field_s[0] == 'hcl'):
            if (not bool(re.match('^#([0-9a-f]{6})$', field_s[1]))):
                return False
        elif (field_s[0] == 'byr'):
            num = int(field_s[1])
            if (num < 1920 or num > 2002):
                return False
        elif (field_s[0] == 'iyr'):
            num = int(field_s[1])
            if (num < 2010 or num > 2020):
                return False
        elif (field_s[0] == 'hgt'):
            unit = field_s[1][-2:]
            if (unit == 'cm'):
                num = int(field_s[1].split('cm')[0])
                if (num < 150 or num > 193):
                    return False
            elif (unit == 'in'):
                num = int(field_s[1].split('in')[0])
                if (num < 59 or num > 76):
                    return False
            else:
                return False
    return True

passports = []
pp = []
with open('inputs/4.txt') as f:
    for line in f:
        if (line == '\n'):
            passports.append(' '.join(pp))
            pp = []
        else:
            pp.append(line.strip())

required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

valid_count = 0
for pp in passports:
    if (has_required(pp)):
        if (is_valid(pp)):
            valid_count += 1
print(valid_count)