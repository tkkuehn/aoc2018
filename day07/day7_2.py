#!/usr/bin/python3

import string

num_workers = 5
time_const = 60

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    prereq_index = {}
    ordered_steps = []

    # Parse everything we need to know about the steps
    for record in contents:
        focal_step = record[36]
        prereq = record[5]

        if prereq not in prereq_index:
            prereq_index[prereq] = {}
            prereq_index[prereq]['prereqs'] = set()
            prereq_index[prereq]['length'] = string.ascii_uppercase.index(prereq) + 1 + time_const
            prereq_index[prereq]['done'] = 0

        if focal_step in prereq_index:
            prereq_index[focal_step]['prereqs'].add(prereq)
        else:
            prereq_index[focal_step] = {}
            prereq_index[focal_step]['prereqs'] = set([prereq])
            prereq_index[focal_step]['length'] = string.ascii_uppercase.index(focal_step) + 1 + time_const
            prereq_index[focal_step]['done'] = 0

    completed = set()

    # How many steps are there?
    jobs = len(prereq_index)
    time_taken = 0

    # What are we working on?
    worker_status = [''] * num_workers

    while len(completed) < jobs:
        # Which steps are ready?
        candidates = []
        for focal_step in prereq_index:
            if len(prereq_index[focal_step]['prereqs'] - completed) == 0:
                candidates.append(focal_step)

        # Which steps are in progress?
        candidates.sort()
        for ongoing_job in worker_status:
            if ongoing_job is not '':
                candidates.remove(ongoing_job)

        # Make each elf do their step
        for i in range(num_workers):
            if worker_status[i] is not '':
                to_do = worker_status[i]
                prereq_index[to_do]['done'] += 1
                if prereq_index[to_do]['done'] >= prereq_index[to_do]['length']:
                    completed.add(to_do)
                    del prereq_index[to_do]
                    worker_status[i] = ''
            elif len(candidates) > 0:
                to_do = candidates.pop(0)
                prereq_index[to_do]['done'] += 1
                if prereq_index[to_do]['done'] >= prereq_index[to_do]['length']:
                    completed.add(to_do)
                    del prereq_index[to_do]
                else:
                    worker_status[i] = to_do

        time_taken += 1

    print(time_taken)
