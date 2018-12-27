#!/usr/bin/python3

import itertools

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()
    int_contents = [int(x) for x in contents]

    currentfreq = 0
    freqs = set()
    freq_cycle = iter(itertools.cycle(int_contents))
    while currentfreq not in freqs:
        freqs.add(currentfreq)
        currentfreq += next(freq_cycle)

    print(currentfreq)

