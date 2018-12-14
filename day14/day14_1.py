#!/usr/bin/python3

num_recipes = 513401

scores = [3, 7]
elf_1_index = 0
elf_2_index = 1

score_len = 2
t = 0

# print(f't: {t}, elf 1 index: {elf_1_index}, elf 2 index: {elf_2_index}')
while score_len < (num_recipes + 10):
    elf_1_score = scores[elf_1_index]
    elf_2_score = scores[elf_2_index]

    # Add new recipes to the scoreboard
    score_sum = elf_1_score + elf_2_score
    # print(f'score sum: {score_sum}')
    sum_str = str(score_sum)
    for digit in sum_str:
        scores.append(int(digit))

    # Pick new recipes
    score_len = len(scores)
    elf_1_index = (elf_1_index + 1 + elf_1_score) % score_len
    elf_2_index = (elf_2_index + 1 + elf_2_score) % score_len
    # print(''.join([str(x) for x in scores]))
    t += 1
    # print(f't: {t}, elf 1 index: {elf_1_index}, elf 2 index: {elf_2_index}')


print(''.join([str(x) for x in scores[num_recipes:num_recipes + 10]]))
