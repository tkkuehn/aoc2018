#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    parsed_contents = [claim.replace('#','').replace('@ ', '').replace(',', ' ').replace(':', '').replace('x', ' ').split(' ')[1:5] for claim in contents]
    parsed_contents = [[int(x) for x in claim] for claim in parsed_contents]

    counts = {}

    for claim in parsed_contents:
        x_indices = range(claim[0], claim[0] + claim[2])
        y_indices = range(claim[1], claim[1] + claim[3])

        for i in x_indices:
            for j in y_indices:
                if (i, j) in counts:
                    counts[(i, j)] += 1
                else:
                    counts[(i, j)] = 1

    overlaps = 0
    for key in counts:
        if counts[key] > 1:
            overlaps += 1

    print(overlaps)

