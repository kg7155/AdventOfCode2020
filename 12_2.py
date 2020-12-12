""" Day 12: Rain Risk """
#PART TWO

def rotate(dir):
    global waypoint_location
    dirs = 'WNES'
    to_change = []
    for d, val in waypoint_location.items():
        if (val != 0):
            to_change.append((d,val))
    changed = []
    if (dir == 'L'):
        for d, val in to_change:
            idx = dirs.index(d)
            if (idx <= 0):
                changed.append(('S', val))
            else:
                changed.append((dirs[idx-1], val))
    elif (dir == 'R'):
        for d, val in to_change:
            idx = dirs.index(d)
            if (idx >= 3):
                changed.append(('W', val))
            else:
                changed.append((dirs[idx+1], val))
    
    waypoint_location = {x:0 for x in waypoint_location}
    for d, val in changed:
        waypoint_location[d] = val

def move_ship(factor):
    for d, val in waypoint_location.items():
        if (val != 0):
            rev_dir = get_rev_dir(d)
            ship_location[d] += factor*val - ship_location[rev_dir]
            ship_location[rev_dir] = ship_location[rev_dir] - factor*val
            if (ship_location[rev_dir] <= 0):
                ship_location[rev_dir] = 0
            if (ship_location[d] <= 0):
                ship_location[d] = 0

def move_waypoint(dir, val):
    rev_dir = get_rev_dir(dir)
    waypoint_location[dir] += val - waypoint_location[rev_dir]
    waypoint_location[rev_dir] = waypoint_location[rev_dir] - val
    if (waypoint_location[rev_dir] <= 0):
        waypoint_location[rev_dir] = 0
    if (waypoint_location[dir] <= 0):
        waypoint_location[dir] = 0

def get_rev_dir(dir):
    dirs = 'WNES'
    rev_dirs = 'ESWN'
    idx = dirs.index(dir)
    return rev_dirs[idx]

ship_location = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
waypoint_location = {'N': 1, 'S': 0, 'W': 0, 'E': 10}

with open('inputs/12.txt') as f:
    for instruction in f:
        inst_type = instruction[0]
        inst_val = int(instruction[1:])
        if (inst_type == 'L' or inst_type == 'R'):
            times = int(inst_val/90)
            for i in range(0, times):
                rotate(inst_type)
        elif (inst_type == 'F'):
            move_ship(inst_val)
        else: 
            move_waypoint(inst_type, inst_val)

m_dist = 0
for dir, val in ship_location.items():
    m_dist += val
print(m_dist)