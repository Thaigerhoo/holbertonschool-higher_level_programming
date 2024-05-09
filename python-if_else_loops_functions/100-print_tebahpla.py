#!/usr/bin/python3
count = 0
for i in range(122, 96, -1):
    if count % 2 == 0:
        output += chr(i)
    else:
        output += chr(i - 32)
    count += 1
    if count == 26:
        break

print("{}".format(output))
