def run_program():
    instr_idx = 0
    acc = 0
    while (True):
        instr = instructions[instr_idx]
        instr_type = instr[0]
        instr_num = instr[1]
        instr_flag = instr[2]

        # if there is an infinite loop
        if (instr_flag == 1):
            return True
        
        # set 'visited' flag
        instructions[instr_idx][2] = 1
        
        if (instr_type == 'acc'):
            acc += instr_num
            instr_idx += 1
        elif (instr_type == 'jmp'):
            instr_idx += instr_num
        elif (instr_type == 'nop'):
            instr_idx += 1

        # check if it was the last
        if (instr_idx > last_idx):
            print(acc)
            return False

instructions = []
with open('inputs/8.txt') as f:
    for line in f:
        s = line.strip().split(' ')
        inst = s[0]
        if (s[1][0] == '+'):
            num = int(s[1][1:])
        else:
            num = int(s[1])
        instructions.append([inst, num, 0, 0])

last_idx = len(instructions)-1
changed_idx = 0
while (True):
    # change instruction
    for i in range(0, len(instructions)):
        if (instructions[i][0] == 'jmp' and instructions[i][3] == 0):
            instructions[i][0] = 'nop'
            instructions[i][3] = 1
            changed_idx = i
            break
        elif (instructions[i][0] == 'nop' and instructions[i][3] == 0):
            instructions[i][0] = 'jmp'
            instructions[i][3] = 1
            changed_idx = i
            break
    # run program
    if (not run_program()):
        break
    # change back
    if (instructions[changed_idx][0] == 'jmp'):
        instructions[changed_idx][0] = 'nop'
    elif (instructions[changed_idx][0] == 'nop'):
        instructions[changed_idx][0] = 'jmp'
    # reset visited
    for instr in instructions:
        instr[2] = 0