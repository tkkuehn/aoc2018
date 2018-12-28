#!/usr/bin/python3

a = 0
b = 1
c = 1
d = 10550400
e = 10551293

while True:
    d = b * c
    if d == e:
        a += c
    b += 1
    if b > e:
        c += 1
        if c > e:
            break
        b = 1
    print(f'a: {a}, b: {b}, c: {c}, d: {d}, e: {e}')

