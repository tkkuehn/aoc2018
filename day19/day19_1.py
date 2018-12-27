#!/usr/bin/python3

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

function_map = {
        'addr': addr,
        'addi': addi,
        'mulr': mulr,
        'muli': muli,
        'banr': banr,
        'bani': bani,
        'borr': borr,
        'bori': bori,
        'setr': setr,
        'seti': seti,
        'gtir': gtir,
        'gtri': gtri,
        'gtrr': gtrr,
        'eqir': eqir,
        'eqri': eqri,
        'eqrr': eqrr}

registers = [0, 0, 0, 0, 0, 0]
i = 0

instruction = contents[0]
ip_reg = int(instruction[-1])

contents = contents[1:]

while True:
    instruction = ''
    pointer = registers[ip_reg]
    if (pointer >= len(contents)) or (pointer < 0):
        break
    instruction = contents[pointer]

    split_func = instruction.split(' ')
    function_str = split_func[0]
    func = function_map[function_str]
    a = int(split_func[1])
    b = int(split_func[2])
    c = int(split_func[3])
    registers = func(registers, a, b, c)

    registers[ip_reg] += 1

print(registers[0])
