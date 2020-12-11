""" Day 11: Seating System """
# PART TWO

import numpy as np

def check_direction(x, y, dir):
    occupied_count = 0
    while (x >= 0 and x < h and y >= 0 and y < w):
        if (ferry[x][y] != '.'):
            if (ferry[x][y] == '#'):
                occupied_count +=1
            break
        if ('u' in dir):
            x -= 1
        if ('d' in dir):
            x += 1
        if ('l' in dir):
            y -= 1
        if ('r' in dir):
            y += 1

    return occupied_count

def simulate():
    global ferry
    has_changed = False
    new_ferry = ferry.copy()

    for i in range(0, h):
        for j in range(0, w):
            if (ferry[i][j] == '.'):
                continue
            occupied_count = 0
            occupied_count += check_direction(i-1, j-1, 'lu')
            occupied_count += check_direction(i-1, j, 'u')
            occupied_count += check_direction(i-1, j+1, 'ru')
            occupied_count += check_direction(i, j-1, 'l')
            occupied_count += check_direction(i, j+1, 'r')
            occupied_count += check_direction(i+1, j-1, 'ld')
            occupied_count += check_direction(i+1, j, 'd')
            occupied_count += check_direction(i+1, j+1, 'rd')

            if (ferry[i][j] == 'L' and occupied_count <= 0):
                new_ferry[i][j] = '#'
                has_changed = True
            elif (ferry[i][j] == '#' and occupied_count >= 5):
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