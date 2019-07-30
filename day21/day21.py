import math

def program(target):
    ds_seen = set()
    repeated_es = 0

    d = 0x6b7018
    e = 0x10000

    prev_d = d
    while True:
        # add to d e truncated to 2 hex digits
        d = d + (e & 0xff)

        # truncate d to 6 hex digits
        d = d & 0xffffff

        # multiply d by some magic number
        d = d * 0x1016b

        # truncate d to 6 hex digits
        d = d & 0xffffff

        # check if e is small enough then see if d is the target value
        if (e < 0x100):
            if (d == target):
                break
            else:
                e = d | 0x010000

                if d in ds_seen:
                    print('repeat found: {:}'.format(prev_d))
                    return len(ds_seen)
                
                ds_seen.add(d)
                prev_d = d

                d = 0x6b7018
        else:
             e = e >> 8

    print('done')
    return len(ds_seen)

print(program(7877093))
