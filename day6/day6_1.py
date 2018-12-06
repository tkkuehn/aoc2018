#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    given_points = set([(int(x.split(',')[0]), int(x.split(',')[1]))
        for x in contents])

    distance = 1

    claimed = set()
    equidistant = set()
    closest_points = {}
    points_claimed = {}
    infinite = set()

    for point in given_points:
        points_claimed[point] = set()

    unfinished_points = given_points

    inf_size = 500
    while distance < inf_size:
        claimed_this_time = set()
        points_to_remove = set()
        for point in unfinished_points:
            claimed_new_point = False
            for x_distance in range(distance + 1):
                for multiplier in [-1, 1]:
                    new_point = (point[0] + (multiplier * x_distance),
                            point[1] + (multiplier * (distance - x_distance)))
                    if new_point in claimed:
                        pass # Don't do anything
                    elif new_point in claimed_this_time:
                        equidistant.add(new_point)
                        points_claimed[closest_points[new_point][0]].remove(
                                new_point)
                        closest_points[new_point].append(point)
                    else:
                        closest_points[new_point] = [point]
                        points_claimed[point].add(new_point)
                        claimed_this_time.add(new_point)
                        claimed_new_point = True
            if not claimed_new_point:
                points_to_remove.add(point)
        claimed = claimed | claimed_this_time
        unfinished_points -= points_to_remove
        distance += 1

    for point in given_points:
        for x_distance in range(distance + 1):
            for multiplier in [-1, 1]:
                new_point = (point[0] + (multiplier * x_distance),
                        point[1] + (multiplier * (distance - x_distance)))
                if new_point in claimed:
                    pass # Don't do anything
                else:
                    infinite.add(point)

    max_area = 0
    largest_area = (0, 0)
    for point in (given_points - infinite):
        if len(points_claimed[point]) > max_area:
            max_area = len(points_claimed[point])
            largest_area = point

    print(max_area)
