""" Day 9: Encoding Error """
from itertools import combinations 

numbers = open('inputs/9.txt','r').read().split('\n')
numbers = [int(num) for num in numbers] 

preamble = 25
invalid_num = -1
for i in range(preamble, len(numbers)):
    combs = list(combinations(numbers[i-preamble:i], 2))
    combs = [comb for comb in combs if comb[0] != comb[1]]
    curr_num = numbers[i]
    is_found = 0
    for comb in combs:
        comb_sum = comb[0] + comb[1]
        if (curr_num == comb_sum):
            is_found = 1
            break
    if (not is_found):
        invalid_num = curr_num
        break

# PART ONE
#print(invalid_num)

window = 2
not_found = True
while (not_found):
    for i in range(0, len(numbers)):
        l = numbers[i:i+window]
        if (sum(l) == invalid_num):
            not_found = False
            # PART TWO
            print(min(l) + max(l))
    window += 1