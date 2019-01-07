#!/usr/bin/python3

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

regex = contents[0][1:-1]

def parse_regex(regex):
    print(len(regex))
    paths = []
    current_paths = [[]]
    i = 0
    while i < len(regex):
        c = regex[i]
        if c in ['N', 'E', 'S', 'W']:
            for path in current_paths:
                path.append(c)
        elif c == '(':
            next_paths, increment = parse_regex(regex[i + 1:])
            new_paths = []
            for path in current_paths:
                for next_path in next_paths:
                    new_paths.append(path + next_path)
            current_paths = new_paths
            i += increment + 1
        elif c == ')':
            paths.extend(current_paths.copy())
            return (paths, i)
        elif c == '|':
            paths.extend(current_paths.copy())
            current_paths = [[]]
        i += 1
    paths.extend(current_paths.copy())
    return (paths, i)

def take_2(regex):
    strings = []
    substring = []
    i = 0
    while i < len(regex):
        c = regex[i]
        if c in ['N', 'E', 'S', 'W']:
            substring.append(c)
        elif c == '(':
            next_string, increment = take_2(regex[i + 1:])
            substring.append(next_string)
            i += increment + 1
        elif c == ')':
            strings.append(substring.copy())
            return (strings, i)
        elif c == '|':
            strings.append(substring.copy())
            substring = []
        i += 1
    strings.append(substring.copy())
    return (strings, i)

def parse_list(regex_list):
    paths = []
    current_paths = [[]]
    for path in regex_list:
        for el in path:
            if el in ['N', 'E', 'S', 'W']:
                for cur_path in current_paths:
                    cur_path.append(el)
            elif len(el) > 0:
                new_paths = []
                extensions = parse_list(el)
                for cur_path in current_paths:
                    for extension in extensions:
                        new_paths.append(cur_path + extension)
                current_paths = new_paths
        paths.extend(current_paths.copy())
        current_paths = [[]]

    return paths

def follow_routes(regex_list, starting_points, connections):
    for path in regex_list:
        for el in path:
            if el in ['N', 'E', 'S', 'W']:
                next_points = set()
                for point in starting_points:
                    next_point = point
                    if el == 'N':
                        next_point = (point[0], point[1] + 1)
                    elif el == 'E':
                        next_point = (point[0] + 1, point[1])
                    elif el == 'S':
                        next_point = (point[0], point[1] - 1)
                    elif el == 'W':
                        next_point = (point[0] - 1, point[1])

                    if point in connections:
                        connections[point].add(next_point)
                    else:
                        connections[point] = set([next_point])
                    next_points.add(next_point)
            else:
                starting_points, connections = follow_routes(
                        el, starting_points, connections)


