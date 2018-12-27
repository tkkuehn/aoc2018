#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()[0].split(' ')

    num_players = int(contents[0])
    num_marbles = int(contents[6]) + 1

    circle = [0]
    scores = [0] * num_players

    player_index = 0
    current_marble = 0
    for marble in range(num_marbles):
        if marble == 0:
            pass
        elif marble % 23 == 0:
            scores[player_index] += marble
            to_remove = (current_marble - 7) % len(circle)
            scores[player_index] += circle.pop(to_remove)
            current_marble = to_remove
        else:
            circle.insert((current_marble + 2) % len(circle), marble)
            current_marble = circle.index(marble)
        player_index += 1
        player_index %= num_players

    print(max(scores))

