""" Day 13: Shuttle Search """
# PART ONE

with open('inputs/13.txt') as f:
    time = int(f.readline())
    ids = list(f.readline().split(','))

while 'x' in ids:
    ids.remove('x')
ids = map(int, ids)

min_diff = float('inf')
min_id = -1
for id in ids:
    diff = (int(time/id) + 1)*id - time
    if (diff < min_diff):
        min_diff = diff
        min_id = id
print(min_id * min_diff)