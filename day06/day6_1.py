#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    given_points = set([(int(x.split(',')[0]), int(x.split(',')[1]))
        for x in contents])
    claimed_points = set()
    contested_points = set()
    claimed_index = {}

    for point in given_points:
        claimed_index[point] = set()

    distance = 1

    infinite = set()

    unfinished_points = given_points

    # Just some large number
    inf_size = 250

    while distance < inf_size:
        known_points = given_points | claimed_points | contested_points
        claims_index = {}
        for point in given_points:
            for x_distance in range(distance + 1):
                for x_multiplier in [-1, 1]:
                  for y_multiplier in [-1, 1]:
                    new_point = (point[0] + (x_multiplier * x_distance),
                            point[1] + (y_multiplier * (distance - x_distance)))
                    if new_point in known_points:
                        pass # Don't do anything
                    else:
                        if new_point in claims_index:
                            claims_index[new_point].add(point)
                        else:
                            claims_index[new_point] = set([point])
        for new_point in claims_index:
            if len(claims_index[new_point]) > 1:
                contested_points.add(new_point)
                    
            else:
                claimed_points.add(new_point)
                claimer = claims_index[new_point].pop()
                claimed_index[claimer].add(new_point)

                # If still claiming points, this point is probably infinite
                if distance == inf_size - 1:
                    infinite.add(claimer) 
        distance += 1
            
    max_area = 0
    largest_area = (0, 0)
    for point in (given_points - infinite):
        if len(claimed_index[point]) > max_area:
            max_area = len(claimed_index[point]) + 1
            largest_area = point

    print(max_area)
