#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}".format(chr(97 + i) if i % 2 == 0 else chr(65 + i)), end="")
