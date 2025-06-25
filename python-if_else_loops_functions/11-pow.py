#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    result = 1
    exp = abs(b)
    for _ in range(exp):
        result *= a
    return 1 / result if b < 0 else result
