#!/usr/bin/python3

import string
import numpy 

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()
    
    two_count = 0
    three_count = 0

    for id in contents:
        found_two = False
        found_three = False
        for letter in string.ascii_lowercase:
            if not found_two and id.count(letter) == 2:
                two_count += 1
                found_two = True
            elif not found_three and id.count(letter) == 3:
                three_count += 1
                found_three = True

            if found_two and found_three:
                break

    print(two_count * three_count)

