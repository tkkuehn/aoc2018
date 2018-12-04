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

    guard_mins_asleep = {}
    for guard in guards:
        mins_asleep = 0
        for shift in guards[guard]:
            mins_asleep += sum(schedules[shift]['asleep'])

        guard_mins_asleep[guard] = mins_asleep

    max_mins_asleep = 0
    sleepiest_guard_id = 0
    for guard in guard_mins_asleep:
        if guard_mins_asleep[guard] > max_mins_asleep:
             max_mins_asleep = guard_mins_asleep[guard]
             sleepiest_guard_id = guard

    minutes_slept = [schedules[date]['asleep'] for date in 
        guards[sleepiest_guard_id]]
    shifts_slept = [sum(x) for x in zip(*minutes_slept)]
   
    print(sleepiest_guard_id)
    print(max(shifts_slept))
    print(shifts_slept.index(max(shifts_slept))) 
    print(shifts_slept.index(max(shifts_slept)) * int(sleepiest_guard_id))

