#!/usr/bin/python3


contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

track = {}
carts = []

y_len = len(contents)
x_len = max([len(x) for x in contents])

for i in range(len(contents)):
    line = contents[i]
    for j in range(len(line)):
        section = line[j]
        if section == '|':
            track[(j, i)] = 'vertical'
        elif section == '-':
            track[(j, i)] = 'horizontal'
        elif section == '^':
            track[(j, i)] = 'vertical'
            carts.append({'pos': (j, i), 'facing': 'up'})
        elif section == 'v':
            track[(j, i)] = 'vertical'
            carts.append({'pos': (j, i), 'facing': 'down'})
        elif section == '>':
            track[(j, i)] = 'horizontal'
            carts.append({'pos': (j, i), 'facing': 'right'})
        elif section == '<':
            track[(j, i)] = 'horizontal'
            carts.append({'pos': (j, i), 'facing': 'left'})
        elif section == '\\':
            if (j + 1 < len(line)) and line[j + 1] in ('-', '<', '>', '+'):
                track[(j, i)] = 'up/right'
            else:
                track[(j, i)] = 'down/left'
        elif section == '/':
            if (j + 1 < len(line)) and line[j + 1] in ('-', '<', '>', '+'):
                track[(j, i)] = 'down/right'
            else:
                track[(j, i)] = 'up/left'
        elif section == '+':
            track[(j, i)] = 'junction'
        elif section == ' ':
            pass
        else:
            print(f'Unknown character: {section}')

for j in range(y_len):
    line = []
    for i in range(x_len):
        if (i, j) in track:
            if track[(i, j)] == 'vertical':
                line.append('|')
            elif track[(i, j)] == 'horizontal':
                line.append('-')
            elif track[(i, j)] == 'junction':
                line.append('+')
            elif track[(i, j)] in ['up/right', 'down/left']:
                line.append('\\')
            elif track[(i, j)] in ['down/right', 'up/left']:
                line.append('/')
        else:
            line.append(' ')
#    print(''.join(line))

for cart in carts:
    cart['next_turn'] = 'left'

collision = False
collision_site = (0, 0)
t = 0
while not collision:
    carts.sort(key=lambda cart: cart['pos'][1])

    for cart in carts:
        pos = cart['pos']
        facing = cart['facing']

        next_pos = pos
        track_type = track[pos]

        if track_type == 'vertical':
            if facing == 'up':
                next_pos = (pos[0], pos[1] - 1)
            else:
                next_pos = (pos[0], pos[1] + 1)
        elif track_type == 'horizontal':
            if facing == 'right':
                next_pos = (pos[0] + 1, pos[1])
            else:
                next_pos = (pos[0] - 1, pos[1])
        elif track_type == 'up/right':
            if facing == 'down':
                next_pos = (pos[0] + 1, pos[1])
                facing = 'right'
            else:
                next_pos = (pos[0], pos[1] - 1)
                facing = 'up'
        elif track_type == 'up/left':
            if facing == 'down':
                next_pos = (pos[0] - 1, pos[1])
                facing = 'left'
            else:
                next_pos = (pos[0], pos[1] - 1)
                facing = 'up'
        elif track_type == 'down/right':
            if facing == 'up':
                next_pos = (pos[0] + 1, pos[1])
                facing = 'right'
            else:
                next_pos = (pos[0], pos[1] + 1)
                facing = 'down'
        elif track_type == 'down/left':
            if facing == 'up':
                next_pos = (pos[0] - 1, pos[1])
                facing = 'left'
            else:
                next_pos = (pos[0], pos[1] + 1)
                facing = 'down'
        elif track_type == 'junction':
            if cart['next_turn'] == 'left':
                if facing == 'up':
                    next_pos = (pos[0] - 1, pos[1])
                    facing = 'left'
                elif facing == 'right':
                    next_pos = (pos[0], pos[1] - 1)
                    facing = 'up'
                elif facing == 'down':
                    next_pos = (pos[0] + 1, pos[1])
                    facing = 'right'
                elif facing == 'left':
                    next_pos = (pos[0], pos[1] + 1)
                    facing = 'down'
                cart['next_turn'] = 'straight'
            elif cart['next_turn'] == 'straight':
                if facing == 'up':
                    next_pos = (pos[0], pos[1] - 1)
                elif facing == 'right':
                    next_pos = (pos[0] + 1, pos[1])
                elif facing == 'down':
                    next_pos = (pos[0], pos[1] + 1)
                elif facing == 'left':
                    next_pos = (pos[0] - 1, pos[1])
                cart['next_turn'] = 'right'
            elif cart['next_turn'] == 'right':
                if facing == 'up':
                    next_pos = (pos[0] + 1, pos[1])
                    facing = 'right'
                elif facing == 'right':
                    next_pos = (pos[0], pos[1] + 1)
                    facing = 'down'
                elif facing == 'down':
                    next_pos = (pos[0] - 1, pos[1])
                    facing = 'left'
                elif facing == 'left':
                    next_pos = (pos[0], pos[1] - 1)
                    facing = 'up'
                cart['next_turn'] = 'left'
        else:
            print(f'Unknown track type: {track_type}')
        cart['pos'] = next_pos
        cart['facing'] = facing

        cart_positions = set()
        for new_cart in carts:
            cart_pos = new_cart['pos']
            if cart_pos in cart_positions:
                collision = True
                collision_site = cart_pos
                break
            else:
                cart_positions.add(cart_pos)

    t += 1

print(collision_site)

