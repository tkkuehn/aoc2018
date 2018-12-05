#!/usr/bin/python3

import string

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()
    orig_polymer = contents[0]

    shortest_length = 99999 # Bigger than previous answer

    for letter in string.ascii_lowercase:
        polymer = orig_polymer
        polymer = polymer.replace(letter, '')
        polymer = polymer.replace(letter.swapcase(), '')

        t = 0

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

        if len(polymer) < shortest_length:
            shortest_length = len(polymer)

    print(shortest_length)

