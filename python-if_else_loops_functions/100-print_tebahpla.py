#!/usr/bin/python3
count = 0
for i in range(122, 96, -1):
    if count % 2 == 0:
        print(chr(i), end='')
    else:
        print(chr(i - 32), end='')
