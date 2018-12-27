#!/usr/bin/python3

import datetime

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    contents.sort()

    current_id = 0
    schedules = {}
    guards = {}

    for record in contents:
        date = record[1:11]
        hour = record[12:14]
        minute = record[15:17]
        content = record[19:]
        key = content[0:5]

        dt = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        
        if key == 'Guard':
            current_id = record[26:26 + record[26:].find(' ')]
            if hour != '00':
                current_date = dt + datetime.timedelta(days = 1)
            else:
                current_date = dt

            schedules[current_date] = {'id': current_id, 'asleep': [0] * 60}
            if current_id in guards:
                guards[current_id].append(current_date)
            else:
                guards[current_id] = [current_date]

        elif key == 'falls':
            schedules[dt]['asleep'][int(minute):] = [1] * (60 - int(minute))

        elif key == 'wakes':
            schedules[dt]['asleep'][int(minute):] = [0] * (60 - int(minute))

    most_consistent_sleeper = 0
    num_times_slept = 0
    most_slept_minute = 0

    for guard in guards:
        minutes_slept = [schedules[date]['asleep'] for date in 
            guards[guard]]
        shifts_slept = [sum(x) for x in zip(*minutes_slept)]
        if max(shifts_slept) > num_times_slept:
            most_consistent_sleeper = guard
            num_times_slept = max(shifts_slept)
            most_slept_minute = shifts_slept.index(num_times_slept)
   
    print(most_slept_minute * int(most_consistent_sleeper))

