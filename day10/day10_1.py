#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    pos_tuples = [(int(x[10:16].strip()), int(x[18:24].strip()), int(x[36:38].strip()), int(x[40:42].strip())) for x in contents]

    vel_dict = {}
    pos_dict = {}
    for record in pos_tuples:
        # Assuming every initial position is unique
        pos_dict[record[0:2]] = record[0:2]
        vel_dict[record[0:2]] = record[2:4]

    current_pos = set()

    while True:
        current_pos.clear()
        for init_pos in pos_dict:
            pos = pos_dict[init_pos]
            vel = vel_dict[init_pos]
            next_x = pos[0] + vel[0]
            next_y = pos[1] + vel[1]
            pos_dict[init_pos] = (next_x, next_y)
            current_pos.add((next_x, next_y))

        # Message is probably there if every current position has a neighbour
        all_neighbours = True
        for init_pos in pos_dict:
            has_neighbour = False
            pos = pos_dict[init_pos]
            for x_change in [-1, 0, 1]:
                for y_change in [-1, 0, 1]:
                    neighbour = (pos[0] + x_change, pos[1] + y_change)
                    if (x_change, y_change) == (0, 0):
                        pass
                    elif neighbour in current_pos:
                        has_neighbour = True
            if not has_neighbour:
                all_neighbours = False
                break
        if all_neighbours:
            break

    # Now just print the result
    min_x = min([x[0] for x in current_pos])
    max_x = max([x[0] for x in current_pos])
    min_y = min([x[1] for x in current_pos])
    max_y = max([x[1] for x in current_pos])

    for y in range(min_y, max_y + 1):
        message = []
        for x in range(min_x, max_x + 1):
            if (x, y) in current_pos:
                message.append('#')
            else:
                message.append('.')
        print(''.join(message))

