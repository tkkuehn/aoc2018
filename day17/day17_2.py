#!/usr/bin/python3

import collections

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

spring = (500, 0)
clay = set()

for line in contents:
    split_line = line.split(' ')
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    if line[0] == 'x':
        x_min = int(split_line[0][2:-1])
        x_max = x_min
        y_range = split_line[1][2:]
        y = y_range.split('..')
        y_min = int(y[0])
        y_max = int(y[1])
    else:
        y_min = int(split_line[0][2:-1])
        y_max = y_min
        x_range = split_line[1][2:]
        x = x_range.split('..')
        x_min = int(x[0])
        x_max = int(x[1])

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            clay.add((x, y))

x_vals = set([x[0] for x in clay])
x_min = min(x_vals)
x_max = max(x_vals)
y_vals = set([x[1] for x in clay])
y_min = min(y_vals)
y_max = max(y_vals)

def print_state():
    for y in range(y_min, y_max + 1):
        line = []
        for x in range(x_min - 1, x_max + 2):
            point = (x, y)
            if point == spring:
                line.append('+')
            elif point in clay:
                line.append('#')
            elif point in water:
                line.append('~')
            elif point in dry:
                line.append('|')
            else:
                line.append('.')
        print(''.join(line))

def find_bottom(current):
    while True:
        if current[1] + 1 > y_max:
            # we've hit the bottom of our scan
            return (current[0], current[1] + 1)

        next_square = (current[0], current[1] + 1)
        if next_square in dry:
            # don't do anything, just move on
            current = next_square
        elif next_square in water | clay:
            # this is the bottom
            return current
        else:
            # next_square is sand, so water could hypothetically reach it
            dry.add(next_square)
            current = next_square

def spread_water(current):
    to_classify = [current]

    # consider negative direction
    bounded_left = False
    negative_x = -1
    while True:
        next_square = (current[0] + negative_x, current[1])
        if next_square in clay:
            # we've found one wall
            bounded_left = True
            break

        # not blocked, so classify the next square
        to_classify.append(next_square)

        below_next = (next_square[0], next_square[1] + 1)
        if below_next not in water | clay:
            # we're unbounded on this side
            break
        
        # we've got a base and no wall, so spread
        negative_x -= 1

    # consider positive direction
    bounded_right = False
    positive_x = 1
    while True:
        next_square = (current[0] + positive_x, current[1])
        if next_square in clay:
            # we've found a wall
            bounded_right = True
            break

        # not blocked, so classify the next square
        to_classify.append(next_square)

        below_next = (next_square[0], next_square[1] + 1)
        if below_next not in water | clay:
            # we're not bounded on this side
            break

        # we've got a base and no wall, so spread
        positive_x += 1

    return (sorted(to_classify, key=lambda x: x[0]),
            bounded_left,
            bounded_right)

def update_spread(to_classify, bounded_left, bounded_right, queue, water, dry):
    if bounded_left and bounded_right:
        water |= set(to_classify)
        dry -= set(to_classify)
        return

    dry |= set(to_classify)

    if not bounded_right:
        queue.appendleft(to_classify[-1])
    if not bounded_left:
        queue.appendleft(to_classify[0])

clay = frozenset(clay)
water = set()
dry = set()

start_points = set([spring])

change = True
loops = 0
while change:
    prev_water = water.copy()
    prev_dry = dry.copy()

    to_adjust = set()
    for start_point in start_points:
        if start_point in water:
            to_adjust.add(start_point)

    for start_point in to_adjust:
        start_points.remove(start_point)
        start_points.add((start_point[0], start_point[1] - 1))

    spread_queue = collections.deque()
    spread_queue.extendleft(start_points)
    while len(spread_queue) > 0:
        source = spread_queue.pop()
        bottom = find_bottom(source)
        if bottom[1] < y_max:
            to_classify, bounded_left, bounded_right = spread_water(bottom)
            if not (bounded_left and bounded_right):
                start_points.discard(source)
                if not bounded_left:
                    start_points.add(to_classify[0])
                if not bounded_right:
                    start_points.add(to_classify[-1])
            update_spread(
                    to_classify,
                    bounded_left,
                    bounded_right,
                    spread_queue,
                    water,
                    dry)

    if prev_water == water and prev_dry == dry:
        # no change - let the loop end
        change = False
    else:
        change = True

    loops += 1

water = {x for x in water if (x[1] >= y_min) and (x[1] <= y_max)}
print(len(water))
