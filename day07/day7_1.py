#!/usr/bin/python3

import string

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    prereq_index = {}
    ordered_steps = []

    # What are the prerequisites of each step?
    for record in contents:
        focal_step = record[36]
        prereq = record[5]

        if prereq not in prereq_index:
            prereq_index[prereq] = set()

        if focal_step in prereq_index:
            prereq_index[focal_step].add(prereq)
        else:
            prereq_index[focal_step] = set([prereq])

    completed = set()

    for i in range(len(prereq_index)):
        candidates = []

        # Which steps are ready?
        for focal_step in prereq_index:
            if len(prereq_index[focal_step] - completed) == 0:
                candidates.append(focal_step)

        # Alphabetically sort steps
        candidates.sort()

        next_step = candidates.pop(0)
        completed.add(next_step)
        ordered_steps.append(next_step)
        del prereq_index[next_step]
       
    print(''.join(ordered_steps)) 

