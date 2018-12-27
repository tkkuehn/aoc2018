#!/usr/bin/python3

x_len = 50
y_len = 50

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

lumber_area = {}

for y in range(y_len):
    for x in range(x_len):
        lumber_area[(x, y)] = contents[y][x]

def read_area(area_tuple):
    lumber_area = {}
    for y in range(y_len):
        for x in range(x_len):
            lumber_area[(x, y)] = area_tuple[y][x]
    return lumber_area

def print_area(area):
    for y in range(y_len):
        line = []
        for x in range(x_len):
            line.append(area[(x, y)])
        print(''.join(line))

def area_tuple(area):
    lines = []
    for y in range(y_len):
        line = []
        for x in range(x_len):
            line.append(area[(x, y)])
        line_tuple = tuple(line)
        lines.append(line_tuple)
    return tuple(lines)

def neighbours(acre, current_area):
    for x_change in [-1, 0, 1]:
        for y_change in [-1, 0, 1]:
            if (x_change, y_change) == (0, 0):
                continue
            yield (acre[0] + x_change, acre[1] + y_change)

minutes_complete = 0

state_cache = {}
cycle_start = None
repeats = 0
cycle_minute = 0
cycle_length = 0

current_area = lumber_area.copy()
next_area = {}
for minute in range(1000000000):
    print(minute)
    area = area_tuple(current_area)
    if area in state_cache:
        if repeats == 0:
            cycle_start = area
            cycle_minute = minute
            print(cycle_minute)
        elif area == cycle_start:
            cycle_length = repeats - 1
            print(cycle_length)
            break
        repeats += 1
        current_area = read_area(state_cache[area])
        continue
    for x in range(x_len):
        for y in range(y_len):
            acre = current_area[(x, y)]
            num_trees = 0
            num_yards = 0
            num_open = 0
            for neighbour in neighbours((x, y), current_area):
                if neighbour not in current_area:
                    continue
                neighbour_type = current_area[neighbour]
                if neighbour_type == '|':
                    num_trees += 1
                elif neighbour_type == '#':
                    num_yards += 1
                elif neighbour_type == '.':
                    num_open += 1
            if acre == '.':
                if num_trees >= 3:
                    next_area[(x, y)] = '|'
                else:
                    next_area[(x, y)] = '.'
            elif acre == '|':
                if num_yards >= 3:
                    next_area[(x, y)] = '#'
                else:
                    next_area[(x, y)] = '|'
            elif acre == '#':
                if (num_yards >= 1) and (num_trees >= 1):
                    next_area[(x, y)] = '#'
                else:
                    next_area[(x, y)] = '.'
    state_cache[area_tuple(current_area)] = area_tuple(next_area)
    current_area = next_area.copy()
    next_area = {}

cycle_num = round((1000000000 - cycle_minute) / cycle_length)
minute = (cycle_num + 1) * cycle_length
minutes_left = 1000000000 - minute
current_state = read_area(cycle_start)

for i in range(minutes_left):
    area = area_tuple(current_area)
    current_area = read_area(state_cache[area])

num_trees = 0
num_acres = 0
for x in range(x_len):
    for y in range(y_len):
        type = current_area[(x, y)]
        if type == '|':
            num_trees += 1
        elif type == '#':
            num_yards += 1

print_area(current_area)
print(num_trees * num_yards)
