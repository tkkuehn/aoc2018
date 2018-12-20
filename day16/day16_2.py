#!/usr/bin/python3

import ast

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

def addr(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] + registers[b]
    return output

def addi(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] + b
    return output 

def mulr(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] * registers[b]
    return output 

def muli(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] * b
    return output 

def banr(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] & registers[b]
    return output 

def bani(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] & b
    return output 

def borr(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] | registers[b]
    return output 

def bori(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a] | b
    return output 

def setr(registers, a, b, c):
    output = registers.copy()
    output[c] = registers[a]
    return output 

def seti(registers, a, b, c):
    output = registers.copy()
    output[c] = a
    return output 

def gtir(registers, a, b, c):
    output = registers.copy()
    output[c] = int(a > registers[b])
    return output 

def gtri(registers, a, b, c):
    output = registers.copy()
    output[c] = int(registers[a] > b)
    return output 

def gtrr(registers, a, b, c):
    output = registers.copy()
    output[c] = int(registers[a] > registers[b])
    return output 

def eqir(registers, a, b, c):
    output = registers.copy()
    output[c] = int(a == registers[b])
    return output 

def eqri(registers, a, b, c):
    output = registers.copy()
    output[c] = int(registers[a] == b)
    return output 

def eqrr(registers, a, b, c):
    output = registers.copy()
    output[c] = int(registers[a] == registers[b])
    return output

contents_1 = contents[0:contents.index('12 3 3 2')][0:-3]

records = []
for i in range(int((len(contents_1)) / 4) + 1):
    records.append(contents_1[(4 * i):(4 * i) + 3])

test_cases = []
for record in records:
    test_case = {}

    before = record[0]
    test_case['before'] = ast.literal_eval(before[before.index('['):])
    test_cases.append(test_case)

    command = record[1]
    command = command.split(' ')
    test_case['opcode'] = int(command[0])
    test_case['a'] = int(command[1])
    test_case['b'] = int(command[2])
    test_case['c'] = int(command[3])

    after = record[2]
    test_case['after'] = ast.literal_eval(after[after.index('['):])

functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti,
        gtir, gtri, gtrr, eqir, eqri, eqrr]

potential_functions = []
for i in range(16):
    potential_functions.append(set(functions))

for test_case in test_cases:
    registers = test_case['before']
    a = test_case['a']
    b = test_case['b']
    c = test_case['c']
    opcode = test_case['opcode']
    output = test_case['after']
    for function in functions:
        if function(registers, a, b, c) != output:
            potential_functions[opcode].discard(function)

found_functions = set()
while len(found_functions) < 16:
    found_new_function = False
    for i in range(16):
        function_set = potential_functions[i]
        unclaimed_functions = function_set - found_functions
        if len(unclaimed_functions) == 1:
            found_new_function = True
            found_function = unclaimed_functions.copy().pop()
            found_functions.add(found_function)
            potential_functions[i] = unclaimed_functions.copy()
    if not found_new_function:
        break

instructions = contents[contents.index('12 3 3 2'):]
registers = [0, 0, 0, 0]
for instruction in instructions:
    instruction = instruction.split(' ')
    opcode = int(instruction[0])
    a = int(instruction[1])
    b = int(instruction[2])
    c = int(instruction[3])
    registers = potential_functions[opcode].copy().pop()(registers, a, b, c)

print(registers[0])

