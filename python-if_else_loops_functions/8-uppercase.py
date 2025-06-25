#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by new line."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
