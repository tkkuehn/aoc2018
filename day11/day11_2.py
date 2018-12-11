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
#        if (i, j) == (121, 78):
#            print(f'{rack_id} {power_1} {power_2} {power_3} {power_4} {power_5} {grid[(121, 78)]}')

highest_power = 0
highest_point = (0, 0, 1)
point_power = {}

for size in range(1, 301):
    print(size)
    for i in range(301 - size):
        for j in range(301 - size):
            if size > 1:
                total_power = point_power[(i + 1, j + 1, size - 1)]
            else:
                total_power = 0

            for increase in range(size - 1):
                total_power += grid[(i + increase, j + size - 1)]
                total_power += grid[(i + size - 1, j + increase)]
            total_power += grid[(i + size - 1, j + size - 1)]
            
            point_power[(i + 1, j + 1, size)] = total_power
            if total_power > highest_power:
                highest_power = total_power
                highest_point = (i + 1, j + 1, size)

print(highest_point)

