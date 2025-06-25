#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:  # a-z
            print("{}".format(chr(ord(c) - 32)), end='')
        else:
            print("{}".format(c), end='')
    print()
