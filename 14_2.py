""" Day 14: Docking Data """
# PART TWO

import re
import itertools

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
    bin_mem = list(format(mem, f))

    # apply the mask on mem
    float_list = []
    for i in range(0, len(bin_mem)):
        if (mask[i] == '1'):
            bin_mem[i] = '1'
        elif (mask[i] == 'X'):
            bin_mem[i] = 'X'
            float_list.append(i)

    combs = list(itertools.product([0, 1], repeat=len(float_list)))

    # write value to all possible memory addresses
    for comb in combs:
        float_idx = 0
        for bit in comb:
            mem_idx = float_list[float_idx]
            bin_mem[mem_idx] = str(bit)
            float_idx += 1
        dec_mem = binlist_to_dec(bin_mem)
        cells[dec_mem] = val

cells = {}
with open('inputs/14.txt') as f:
    for line in f:
        if ('mask' in line):
            mask = line.strip()[7:]
        else:
            mem_val = re.findall(r'\d+', line)
            mem = int(mem_val[0])
            val = int(mem_val[1])
            write(mem,val)

print(sum(cells.values()))