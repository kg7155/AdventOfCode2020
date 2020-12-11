""" Day 11: Seating System """
# PART ONE

import numpy as np

def simulate():
    global ferry
    has_changed = False
    new_ferry = ferry.copy()

    for i in range(0, h):
        for j in range(0, w):
            if (ferry[i][j] == '.'):
                continue
            adj_occupied_count = 0
            if (i-1 >= 0 and j-1 >= 0):
                if (ferry[i-1][j-1] == '#'):
                    adj_occupied_count += 1
            if (i-1 >= 0 and j >= 0):
                if (ferry[i-1][j] == '#'):
                    adj_occupied_count += 1
            if (i-1 >= 0 and j+1 >= 0) and j+1 < w:
                if (ferry[i-1][j+1] == '#'):
                    adj_occupied_count += 1
            if (i >= 0 and j-1 >= 0):
                if (ferry[i][j-1] == '#'):
                    adj_occupied_count += 1
            if (i >= 0 and j+1 >= 0 and j+1 < w):
                if (ferry[i][j+1] == '#'):
                    adj_occupied_count += 1
            if (i+1 >= 0 and i+1 < h and j-1 >= 0):
                if (ferry[i+1][j-1] == '#'):
                    adj_occupied_count += 1
            if (i+1 >= 0 and i+1 < h and j >= 0):
                if (ferry[i+1][j] == '#'):
                    adj_occupied_count += 1
            if (i+1 >= 0 and i+1 < h and j+1 >= 0 and j+1 < w):
                if (ferry[i+1][j+1] == '#'):
                    adj_occupied_count += 1
            if (ferry[i][j] == 'L' and adj_occupied_count <= 0):
                new_ferry[i][j] = '#'
                has_changed = True
            elif (ferry[i][j] == '#' and adj_occupied_count >= 4):
                new_ferry[i][j] = 'L'
                has_changed = True
    ferry = new_ferry
    return has_changed

with open('inputs/11.txt') as f:
    ferry = [list(line.strip()) for line in f]
ferry = np.array(ferry)
h = len(ferry)
w = len(ferry[0])

while(simulate()):
    pass

occ_count = 0
for i in ferry:
    for j in i:
        if j == '#':
            occ_count += 1

print(occ_count)