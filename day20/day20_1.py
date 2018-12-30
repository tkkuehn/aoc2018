#!/usr/bin/python3

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

regex = contents[0][1:-1]

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def parse_list(substring, depth=0, level_paths=None):
    if len(substring) == 0:
        return [[]]
    c = substring[0]
    if c in set(['N', 'E', 'S', 'W']):
        paths = []
        for path in parse_list(substring[1:], depth, level_paths):
            paths.append([c] + path)
        return paths
    elif c == '(':
        subpaths, length = handle_branch(substring[i + 1:])

        return parse_list(substring[1:], depth + 1, [[]])

root = Node('')
leaves = []

def handle_branch(substring):
    paths = []
    current_root = None
    current_leaf = None
    i = 0
    while True:
        c = substring[i]
        if c in set(['N', 'E', 'S', 'W']):
            next_node = Node(c)
            if not current_root:
                current_root = next_node
                current_leaf = current_root
            else:
                current_leaf.children.append(Node(c))
                current_leaf = current_leaf.children[0]
            current_path = current_path.children[0]
        elif c == '|':
            paths.append(current_path.copy())
            current_path = []
        elif c == ')':
            paths.append(current_path.copy())
            return (paths, i)
        elif c == '(':
            subpaths, length = handle_branch(substring[i + 1:])
            current_path.append(subpaths)
            i += length
        i += 1

