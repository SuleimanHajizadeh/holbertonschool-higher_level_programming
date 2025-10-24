#!/usr/bin/python3
for i in range(25, -1, -1):
    j = 25 - i
    print("{}".format(chr(122 - i) if j % 2 == 0 else chr(90 - i)), end="")
