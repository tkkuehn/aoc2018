#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()
    polymer = contents[0]

    t = 0
    i = 0

    changes_made = True

    while changes_made:
        changes_made = False
        i = 0 

        while i < len(polymer) - 1:
            if polymer[i] == polymer[i + 1].swapcase():
                polymer = polymer.replace(polymer[i] + polymer[i + 1], '', 1)
                changes_made = True
            else:
                # do nothing
                i += 1
        t += 1

