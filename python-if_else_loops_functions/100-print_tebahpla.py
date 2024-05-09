#!/usr/bin/python3
count = 0
output = ""
for i in range(122, 96, -1):
    if count % 2 == 0:
        output += chr(i)
    else:
        output += chr(i - 32)
    count += 1
    if count == 25:  # Stop when 26 characters are printed
        break

print("{}".format(output))
