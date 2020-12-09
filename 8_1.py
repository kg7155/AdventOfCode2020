""" Day 8: Handheld Halting """

instructions = []
with open('inputs/8.txt') as f:
    for line in f:
        s = line.strip().split(' ')
        inst = s[0]
        if (s[1][0] == '+'):
            num = int(s[1][1:])
        else:
            num = int(s[1])
        instructions.append([inst, num, 0])

is_loop = False
instr_idx = 0
acc = 0
while (not is_loop):
    instr = instructions[instr_idx]
    instr_type = instr[0]
    instr_num = instr[1]
    instr_flag = instr[2]

    if (instr_flag == 1):
        is_loop = True
        break
    instructions[instr_idx][2] = 1
    
    if (instr_type == 'acc'):
        acc += instr_num
        instr_idx += 1
    elif (instr_type == 'jmp'):
        instr_idx += instr_num
    elif (instr_type == 'nop'):
        instr_idx += 1
print(acc)