#!/usr/bin/python3

# This comes from an understanding of what the elfcode does - see the rest of
# this day's directory for more

a = 0

for i in range(1, 10551294):
    if (10551293 % i) == 0:
        a += i

print(a)

