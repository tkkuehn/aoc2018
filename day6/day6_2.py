#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    given_points = set([(int(x.split(',')[0]), int(x.split(',')[1]))
        for x in contents])

    x_values = [x[0] for x in given_points]
    y_values = [x[1] for x in given_points]
    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)

    candidates = set()

    for x in range(x_min - 1, x_max + 1):
        for y in range(y_min - 1, y_max + 1):
            current_point = (x, y)
            d_sum = sum([abs(point[0] - current_point[0])
                + abs(point[1] - current_point[1]) for point in given_points])
            if d_sum < 10000:
                candidates.add(current_point)

    print(len(candidates))

