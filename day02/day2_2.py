#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()
    
    id_len = len(contents[0])

    for i in range(id_len):
        short_contents = [x[0:i] + x[i+1:id_len] for x in contents]
        for short_id in short_contents:
            if short_contents.count(short_id) > 1:
                print(short_id)
                break

