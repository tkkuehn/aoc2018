#!/usr/bin/python3


contents = []
with open('./resources/test_input.txt', 'r') as f:
    contents = f.read().splitlines()

track = {}
carts = []

for i in range(len(contents)):
    line = contents[i]
    for j in range(len(line)):
        section = line[j]
        if section == '|':
            track[(i, j)] = 'vertical'
        elif section == '-':
            track[(i, j)] = 'horizontal'
        elif section == '^':
            track[(i, j)] = 'vertical'
            carts.append({'pos': (i, j), 'facing': 'up'})
        elif section == 'v':
            track[(i, j)] = 'vertical'
            carts.append({'pos': (i, j), 'facing': 'down'})
        elif section == '>':
            track[(i, j)] = 'horizontal'
            carts.append({'pos': (i, j), 'facing': 'right'})
        elif section == '<':
            track[(i, j)] = 'horizontal'
            carts.append({'pos': (i, j), 'facing': 'left'})
        elif section == '\\':
            if (j + 1 < len(line)) and line[j + 1] == '-':
                track[(i, j)] = 'up/right'
            else:
                track[(i, j)] = 'down/left'
        elif section == '/':
            if (j + 1 < len(line)) and line[j + 1] == '-':
                track[(i, j)] = 'down/right'
            else:
                track[(i, j)] = 'up/left'
        elif section == '+':
            track[(i, j)] = 'junction'

for cart in carts:
    cart['next_turn'] = 'left'

collision = False
collision_site = (0, 0)
t = 0
while not collision:
    for cart in carts:
        pos = cart['pos']
        facing = cart['facing']
        next_pos = pos
        track_type = track[pos]
        if track_type == 'vertical':
            if facing == 'up':
                next_pos[1] -= 1
            else:
                next_pos[1] += 1
        elif track_type == 'horizontal':
            if facing == 'right':
                next_pos[0] += 1
            else:
                next_pos[0] -= 1
        elif track_type == 'up/right':
            if facing == 'down':
                next_pos[0] += 1
                facing = 'right'
            else:
                next_pos[1] -= 1
                facing = 'up'
        elif track_type == 'up/left':
            if facing == 'down':
                next_pos[0] -= 1
                facing = 'left'
            else:
                next_pos[1] -= 1
                facing = 'up'
        elif track_type == 'down/right':
            if facing == 'up':
                next_pos[0] += 1
                facing = 'right'
            else:
                next_pos[1] += 1
                facing = 'down'
        elif track_type == 'down/left':
            if facing == 'up':
                next_pos[0] -= 1
                facing = 'left'
            else:
                next_pos[1] += 1
                facing = 'down'
        elif track_type == 'junction':
            if cart['next_turn'] == 'left':
                if facing == 'up':
                    next_pos[0] -= 1
                    facing = 'left'
                elif facing == 'right':
                    next_pos[1] -= 1
                    facing = 'up'
                elif facing == 'down':
                    next_pos[0] += 1
                    facing = 'right'
                elif facing == 'left':
                    next_pos[1] += 1
                    facing = 'down'
                cart['next_turn'] = 'straight'
            elif cart['next_turn'] == 'straight':
                if facing == 'up':
                    next_pos[1] -= 1
                elif facing == 'right':
                    next_pos[0] += 1
                elif facing == 'down':
                    next_pos[1] += 1
                elif facing == 'left':
                    next_pos[0] -= 1
                cart['next_turn'] = 'right'
            elif cart['next_turn'] == 'right':
                if facing == 'up':
                    next_pos[0] += 1
                    facing = 'right'
                elif facing == 'right':
                    next_pos[1] += 1
                    facing = 'down'
                elif facing == 'down':
                    next_pos[0] -= 1
                    facing = 'left'
                elif facing == 'left':
                    next_pos[1] -= 1
                    facing = 'up'
                cart['next_turn'] = 'left'
        cart['pos'] = next_pos
        cart['facing'] = facing

    cart_positions = set()
    for cart in carts:
        cart_pos = cart['pos']
        if cart_pos in cart_positions:
            collision = True
            collision_site = cart_pos
        else:
            cart_positions.add(cart_pos)
    t += 1

print(collision_site)

