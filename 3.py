""" Day 3: Toboggan Trajectory """
import numpy as np

def count_trees(slope):
    positions = [(0,0)]
    right = slope[0]
    down = slope[1]
    i = 0
    j = 0
    for n in range (0, int(height/down-1)):
        i += right
        j += down
        if (i >= width):
            i %= width
        positions.append((i, j))

    trees_count = 0
    for pos in positions:
        i = pos[0]
        j = pos[1]
        if (toboggan[j][i] == '#'):
            trees_count += 1
    return trees_count

#toboggan = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.",
#"..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]
with open('inputs/3.txt') as f:
    toboggan = f.read().splitlines() 

height = len(toboggan)
width = len(toboggan[0])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
slopes_trees = []
for slope in slopes:
    slopes_trees.append(count_trees(slope))
print(np.prod(slopes_trees))