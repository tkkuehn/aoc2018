#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    parsed_contents = [claim.replace('#','').replace('@ ', '').replace(',', ' ').replace(':', '').replace('x', ' ').split(' ') for claim in contents]
    parsed_contents = [[int(x) for x in claim] for claim in parsed_contents]

    # count the number of claims at each square
    counts = {}

    for claim in parsed_contents:
        x_indices = range(claim[1], claim[1] + claim[3])
        y_indices = range(claim[2], claim[2] + claim[4])

        for i in x_indices:
            for j in y_indices:
                if (i, j) in counts:
                    counts[(i, j)] += 1
                else:
                    counts[(i, j)] = 1

    # count the number of squares with overlap
    overlaps = 0
    for key in counts:
        if counts[key] > 1:
            overlaps += 1

    # search for the claim with no overlap
    for claim in parsed_contents:
        x_indices = range(claim[1], claim[1] + claim[3])
        y_indices = range(claim[2], claim[2] + claim[4])
        
        overlap = False
        for i in x_indices:
            for j in y_indices:
                if counts[(i, j)] > 1:
                    overlap = True
        if not overlap:
            print(claim[0])

