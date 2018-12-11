#!/usr/bin/python3

serial_number = 7989

# Tried to use a list of lists but couldn't get it working
grid = {}

for i in range(300):
    for j in range(300):
        rack_id = i + 11
        power_1 = rack_id * (j + 1)
        power_2 = power_1 + serial_number
        power_3 = power_2 * rack_id
        power_4 = int(format(power_3, '03')[-3])
        power_5 = power_4 - 5
        grid[(i, j)] = power_5

highest_power = 0
highest_point = (0, 0)

for i in range(298):
    for j in range(298):
        total_power = 0
        for x_increase in [0, 1, 2]:
            for y_increase in [0, 1, 2]:
                total_power += grid[(i + x_increase, j + y_increase)]
        if total_power > highest_power:
            highest_power = total_power
            highest_point = (i + 1, j + 1)

print(highest_point)

