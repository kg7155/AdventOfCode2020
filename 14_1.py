""" Day 14: Docking Data """
# PART ONE

import re

def binlist_to_dec(binlist):
    pos = 0
    sum = 0
    for bit in reversed(binlist):
        if(bit == '1'):
            sum += pow(2,pos)
        pos += 1
    return sum

def write(mem, val):
    # convert to binary format (length of mask)
    f = '0' + str(len(mask)) + 'b'
    bin_val = list(format(val, f))

    # apply the mask on val
    for i in range(0, len(bin_val)):
        if (or_mask[i] == '1'):
            bin_val[i] = '1'
        if (and_mask[i] == '0'):
            bin_val[i] = '0'

    # write value to cell
    cells[mem] = binlist_to_dec(bin_val)

cells = {}
with open('inputs/14.txt') as f:
    for line in f:
        if ('mask' in line):
            mask = line.strip()[7:]
            or_mask = list(mask.replace('X', '0'))
            and_mask = list(mask.replace('X', '1'))
        else:
            mem_val = re.findall(r'\d+', line)
            mem = int(mem_val[0])
            val = int(mem_val[1])
            write(mem,val)

print(sum(cells.values()))