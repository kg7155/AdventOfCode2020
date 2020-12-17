""" Day 16: Ticket Translation """
import re
import operator

field_dict = {}
nearby_tickets = []
read_your_ticket = False
read_nearby_tickets = False
with open('inputs/16.txt') as f:
    for line in f:
        if (read_your_ticket):
            your_ticket = line.strip().split(',')
            your_ticket = [int(t) for t in your_ticket]
            read_your_ticket = False
        elif (read_nearby_tickets):
            nearby_ticket = line.strip().split(',')
            nearby_ticket = [int(t) for t in nearby_ticket]
            nearby_tickets.append(nearby_ticket)
        elif (line != '\n' and 'ticket' not in line):
            line_s = line.split(':')
            field_name = line_s[0]
            ranges = re.findall(r'\d+', line)
            ranges = [int(r) for r in ranges]
            r1 = range(ranges[0], ranges[1]+1)
            r2 = range(ranges[2], ranges[3]+1)
            field_dict[field_name] = [r1, r2, []]
        elif ('your ticket' in line):
            read_your_ticket = True
        elif ('nearby tickets' in line):
            read_nearby_tickets = True

invalid_field_sum = 0
invalid_tickets = []
for nt in nearby_tickets:
    for field in nt:
        is_invalid = True
        for r in field_dict.values():
            if (field in r[0] or field in r[1]):
                is_invalid = False
                break
        if (is_invalid):
            invalid_field_sum += field
            invalid_tickets.append(nt)

# PART ONE
print(invalid_field_sum)

for it in invalid_tickets:
    nearby_tickets.remove(it)

fields = list(field_dict.keys())

for field in fields:
    r1 = field_dict[field][0]
    r2 = field_dict[field][1]
    for pos in range(0, len(fields)):
        field_dict[field][2].append(pos)
        for nt in nearby_tickets:
            if (nt[pos] not in r1 and nt[pos] not in r2):
                field_dict[field][2].remove(pos)
                break

fields_sorted = sorted(field_dict, key=lambda k: len(field_dict[k][2]))
assigned_list = []
for fs in fields_sorted:
    idx_list = field_dict[fs][2]
    for a in assigned_list:
        if a in idx_list:
            field_dict[fs][2].remove(a)
    if (len(idx_list) == 1):
        assigned_list.append(idx_list[0])

positions = [vals[2][0] for k, vals in field_dict.items() if 'departure' in k]
prod = 1
for pos in positions:
    prod *= your_ticket[pos]
# PART TWO
print(prod)