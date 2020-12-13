""" Day 13: Shuttle Search """
# PART TWO

with open('inputs/13.txt') as f:
    timestamp = int(f.readline())
    buses = [(index, int(bus)) for index, bus in enumerate(f.readline().split(',')) if bus != 'x']

timestamp = 0
factor = 1
for offset, bus in buses:
	while (timestamp + offset) % bus:
		timestamp += factor
	factor *= bus
print(timestamp)
