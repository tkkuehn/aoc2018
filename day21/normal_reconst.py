d = 0
while d != 72:
    d = 123
    d = d & 456
d = 0 # 5

# GOTO TARGET (from 30)
e = d | 0b0001_0000_0000_0000_0000 # 6
d = 0b0110_1011_0111_0000_0001_1000 # 7

# GOTO TARGET (from 7 and 27)
f = e & 0b1111_1111 # 8
d = f + d # 9
d = d & 0b1111_1111_1111_1111_1111_1111 # 10
d = d * 65899 # 11
d = d & 0b1111_1111_1111_1111_1111_1111 # 12
f = int(0b0001_0000_0000 > e) # 13
c = 14 + f # 14 (goto 15 or 16)
c = 15 + 1 # 15 (goto 17)
c = 27 # 16 (goto 28)

# GOTO TARGET (from 14/15)
f = 0 # 17

# GOTO TARGET (from 25 or 17)
b = f + 1 # 18
b = b * 256 # 19
b = int(b > e) # 20
c = b + 21 # 21 (goto 22 or 23)
c = 23 # 22 (goto 24)
c = 25 # 23 (goto 26)

# GOTO TARGET (from 21/22)
f = f + 1 # 24
c = 17 # 25 (goto 18)

# GOTO TARGET (from 21/23)
e = f # 26
c = 7 # 27 (goto 8)

# GOTO TARGET (from 14/16)
f = int(a == d) # 28
c = c + f # 29
c = 5 # 30 (goto 6)

