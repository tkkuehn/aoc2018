#!/usr/bin/python3

import math

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

y_num = len(contents)
x_num = len(contents[0])
entities = {}
goblins = []
elves = []
walls = set()

k = 0
for i in range(y_num):
    line = contents[i]
    for j in range(x_num):
        entity = line[j]
        pos = (j, i)
        entities[pos] = entity
        if entity == '#':
            walls.add(pos)
        elif entity == 'G':
            goblins.append(
                    {'id': k, 'type': 'G', 'pos': pos, 'power': 3, 'hp': 200})
            k += 1
        elif entity == 'E':
            elves.append(
                    {'id': k, 'type': 'E', 'pos': pos, 'power': 3, 'hp': 200})
            k += 1

def neighbours(pos):
    x_pos = pos[0]
    y_pos = pos[1]
    for neighbour in [(x_pos, y_pos - 1), (x_pos - 1, y_pos),
            (x_pos + 1, y_pos), (x_pos, y_pos + 1)]:
        yield neighbour

def int_order(pos):
    return (pos[1] * 1000) + (pos[0])

def dijkstra(current):
    open_spaces = set(filter(lambda x: entities[x] == '.',
        entities.keys()))
    unvisited = open_spaces | set([current])
    prevs = {point: [] for point in unvisited}
    dists = {point: math.inf for point in unvisited}
    dists[current] = 0

    while len(unvisited) > 0:
        node = list(sorted(unvisited, key=lambda x: dists[x]))[0]
        unvisited.remove(node)
        node_dist = dists[node]
        for neighbour in neighbours(node):
            alt = node_dist + 1
            if entities[neighbour] != '.':
                continue
            if alt == dists[neighbour]:
                prevs[neighbour].append(node)
            elif alt < dists[neighbour]:
                dists[neighbour] = alt
                prevs[neighbour] = [node]
    return dists

rounds = 0
combat_over = False

while not combat_over:
    units = elves + goblins
    units = sorted(units, key=lambda x: int_order(x['pos']))

    index = 0
    unit_len = len(units)
    while index < unit_len:
        unit = units[index]
        unit_pos = unit['pos']
        unit_type = unit['type']
        targets = []

        if unit_type == 'E':
            targets = goblins
        else:
            targets = elves

        if len(targets) == 0:
            combat_over = True
            break

        # movement step
        in_range = [list(neighbours(x['pos'])) for x in targets]
        in_range = set([item for sublist in in_range for item in sublist])
        if unit_pos in in_range:
            # go to combat
            pass
        else:
            # try to move closer
            in_range = set(filter(
                lambda x: entities[x] == '.',
                in_range))
            if len(in_range) == 0:
                # no targets with free space 
                index += 1
                continue

            # Dijkstra's algorithm to find next step
            dists = dijkstra(unit_pos)
            
            # Okay, we have all the distances now, so what's our target?
            min_dist = math.inf
            min_point = []
            for point in in_range:
                if dists[point] == min_dist:
                    min_point.append(point)
                elif dists[point] < min_dist:
                    min_dist = dists[point]
                    min_point = [point]

            if min_dist == math.inf:
                # no reachable points in range
                index += 1
                continue

            # Target is the one first in reading order
            min_point = sorted(min_point, key=int_order)
            target_point = min_point[0]

            # Take the next step first in reading order
            target_dists = dijkstra(target_point)

            min_dist = math.inf
            min_point = []
            for point in neighbours(unit_pos):
                if entities[point] != '.':
                    continue
                if target_dists[point] == min_dist:
                    min_point.append(point)
                elif target_dists[point] < min_dist:
                    min_dist = target_dists[point]
                    min_point = [point]
            next_pos = sorted(min_point, key=int_order)[0]
            entities[unit_pos] = '.'
            entities[next_pos] = unit_type
            unit['pos'] = next_pos
            unit_pos = next_pos

        # okay, now is combat possible?
        target = ''
        if unit_type == 'E':
            target = 'G'
            targets = goblins
        else:
            target = 'E'
            targets = elves

        defenders = []
        for neighbour in neighbours(unit_pos):
            if entities[neighbour] == target:
                defender_index = [
                        x['pos'] for x in targets].index(neighbour)
                defenders.append(targets[defender_index])
        
        if len(defenders) == 0:
            # still not in range
            pass
        else:
            defender = sorted(defenders,
                    key = lambda x: (x['hp'] * 1000000)
                    + int_order(x['pos']))[0]
            defender['hp'] -= unit['power']
            if defender['hp'] <= 0:
                defender_index = units.index(defender)
                if defender_index < index:
                    index -= 1
                targets.remove(defender)
                units.remove(defender)
                entities[defender['pos']] = '.'
                del defender
                unit_len -= 1
        index += 1

    if not combat_over:
        rounds += 1

winner = ''
total_hp = 0
if len(elves) == 0:
    winner = 'G'
    total_hp = sum([x['hp'] for x in goblins])
else:
    winner = 'E'
    total_hp = sum([x['hp'] for x in elves])

print(rounds * total_hp)

