#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase without using str.upper()."""
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result, end="")
    print()


if __name__ == "__main__":
    uppercase("holberton")
    uppercase("Holberton School")
    uppercase("Holberton School, 98 battery street")
    uppercase("")
    uppercase(98)  # Will raise AttributeError as specified in requirements
