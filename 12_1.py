""" Day 12: Rain Risk """
#PART ONE

def turn(dir):
    global ship_dir
    dirs = 'WNES'
    if (dir == 'L'):
        idx = dirs.index(ship_dir)
        if (idx <= 0):
            ship_dir = 'S'
        else:
            ship_dir = dirs[idx-1]
    elif (dir == 'R'):
        idx = dirs.index(ship_dir)
        if (idx >= 3):
            ship_dir = 'W'
        else:
            ship_dir = dirs[idx+1]

def move(dir, val):
    if (dir == 'F'):
        dir = ship_dir
    rev_dir = get_rev_dir(dir)
    ship_location[dir] += val - ship_location[rev_dir]
    ship_location[rev_dir] = ship_location[rev_dir] - val
    if (ship_location[rev_dir] <= 0):
        ship_location[rev_dir] = 0
    if (ship_location[dir] <= 0):
        ship_location[dir] = 0
    
def get_rev_dir(dir):
    dirs = 'WNES'
    rev_dirs = 'ESWN'
    idx = dirs.index(dir)
    return rev_dirs[idx]

ship_location = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
ship_dir = 'E'
with open('inputs/12.txt') as f:
    for instruction in f:
        inst_type = instruction[0]
        inst_val = int(instruction[1:])
        if (inst_type == 'L' or inst_type == 'R'):
            times = int(inst_val/90)
            for i in range(0, times):
                turn(inst_type)
        else:
            move(inst_type, inst_val)

m_dist = 0
for dir, val in ship_location.items():
    m_dist += val
print(m_dist)