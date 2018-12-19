#!/usr/bin/python3

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

y_num = len(contents)
x_num = len(contents[0])
entities = {}
goblins = []
elves = []
walls = set()

for i in range(y_num):
    line = contents[i]
    for j in range(x_num):
        entity = line[j]
        pos = (j, i)
        entities[pos] = entity
        if entity == '#':
            walls.add(pos)
        elif entity == 'G':
            goblins.append({'type': 'G', 'pos': pos, 'power': 3, 'hp': 200})
        elif entity == 'E':
            elves.append({'type': 'E', 'pos': pos, 'power': 3, 'hp': 200})

def neighbours(pos):
    x_pos = pos[0]
    y_pos = pos[1]
    for neighbour in [(x_pos, y_pos - 1), (x_pos - 1, y_pos),
            (x_pos + 1, y_pos), (x_pos, y_pos + 1)]:
        yield neighbour

def int_order(pos):
    return (pos[1] * 100000) + (pos[0] * 100)

def find_paths(target, current, prevs):
    path_tree = {'point': target, 'children': []}
    if prevs[target] == None:
        return path_tree
    for prev in prevs[target]:
        children.append(find_paths(prev, current, prevs))
    return path_tree

def list_paths(path_tree):
    root = path_tree['point']
    children = path_tree['children']
    paths = []
    if len(children) == 0:
        return [[root]]
    for child in children:
        for path in path_tree(children):
            paths.append(path + [root])
    return paths


combat_over = False
round = 0

while not combat_over:
    units = elves + goblins
    units = sorted(units, key=lambda x: int_order(x['pos']))
    for unit in units:
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
        in_range = set([list(neighbours(x['pos'])) for x in targets])
        if unit_pos in in_range:
            # go to combat
            pass
        else:
            # try to move closer
            in_range = set(filter(
                lambda x: entities[x] == '.',
                set([item for sublist in in_range for item in sublist])))
            if len(in_range) == 0:
                # no targets with free space 
                continue
            open_spaces = set(filter(lambda x: entities[x] == '.',
                entities.keys()))
            unvisited = open_spaces | set([unit_pos])
            prevs = {point: [] for point in unvisited}
            dists = {point: math.inf for point in unvisited}
            dists[unit_pos] = 0

            done = false
            while len(unvisited) > 0:
                node = list(sorted(unvisited, key=lambda x: dist[x]))[0]
                unvisited.remove(node)
                node_dist = dists[node]
                for neighbour in neighbours(node):
                    alt = node_dist + 1
                    if alt == dists[neighbour]:
                        prevs[neighbour].append(node)
                    elif alt < dists[neighbour]:
                        dists[neighbour] = alt
                        prevs[neighbour] = [node]
            
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
                continue

            min_point = sorted(min_point, key=int_order)
            target_point = min_point[0]
            path_tree = find_paths(target_point, unit_pos, prevs)
            path_list = list_paths(path_tree)
            path_list = sorted(path_list, key=lambda x: int_order(x[1]))
            next_pos = path_list[0][1]
            entities[next_pos] = unit_type
            if unit_type == 'E':
                elves[elves.index(unit)]['pos'] = next_pos
            else:
                goblins[goblins.index(unit)]['pos'] = next_pos
            unit['pos'] = next_pos
            unit_pos = next_pos

        # okay, now is combat possible?
        if unit_pos in in_range:
            target = ''
            if unit_type == 'E':
                target = 'G'
            else:
                target = 'E'
            for neighbour in neighbours:
                if entities[neighbour] == target:
                    if unit_type == 'E':
                        goblin_index = [x['pos'] for x in goblins].index(neighbour)
                        goblins[goblin_index]['hp'] -= elves[elves.index(unit)]['power']
                        if goblins[goblin_index]['hp'] <= 0:
                            goblins.pop(goblin_index)
                    else:
                        elf_index = [x['pos'] for x in elves].index(neighbour)
                        elves[elf_index]['hp'] -= goblins[goblins.index(unit)]['power']
                        if elves[elf_index]['hp'] <= 0:
                            elves.pop(elf_index)




        print(in_range)
        break

        # Find shortest path to a 
    combat_over = True
