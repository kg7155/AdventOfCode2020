""" Day 5: Binary Boarding """

def determine_row_col(seat):
    min_row = 0
    max_row = 128
    min_col = 0
    max_col = 8
    for k in seat:
        if (k == 'F'):
            max_row = min_row + (max_row-min_row)/2
        elif (k == 'B'):
            min_row = min_row + (max_row-min_row)/2
        elif (k == 'L'):
            max_col = min_col + (max_col-min_col)/2
        elif (k == 'R'):
            min_col = min_col + (max_col-min_col)/2
    return int(min_row), int(min_col)

with open('inputs/5.txt') as f:
    lines = f.readlines()

max_id = 0
ids = []
for line in lines:
    row, col = determine_row_col(line)
    id = row*8 + col
    ids.append(id)
    if (id > max_id):
        max_id = id

for i in range (min(ids), max_id):
    if (i not in ids):
        print(i)