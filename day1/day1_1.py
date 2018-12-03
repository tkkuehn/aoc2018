#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()
    int_contents = [int(x) for x in contents]
    print(sum(int_contents))

