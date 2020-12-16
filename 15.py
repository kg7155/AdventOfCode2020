""" Day 15: Rambunctious Recitation """

with open('inputs/15.txt') as f:
    starting_nums = f.readline().strip().split(',')

dict_vals = {}
for i in range(0, len(starting_nums)):
    starting_nums[i] = int(starting_nums[i])
    dict_vals[starting_nums[i]] = i+1
    
last_spoken = 0
for i in range (len(dict_vals)+1, 30000001):
    if (last_spoken in dict_vals):
        next = i - dict_vals[last_spoken]
    else:
        next = 0
    answer = last_spoken
    dict_vals[last_spoken] = i
    last_spoken = next
print(answer)