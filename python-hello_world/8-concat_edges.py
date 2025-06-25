#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase without using str.upper()."""
    for char in str:
        diff = 0
        if ord('a') <= ord(char) <= ord('z'):
            diff = 32
        print("{:c}".format(ord(char) - diff), end="")
    print()


if __name__ == "__main__":
    uppercase("holberton")  # HOLBERTON
    uppercase("Holberton School")  # HOLBERTON SCHOOL
    uppercase("Holberton School, 98 battery street")  # HOLBERTON SCHOOL, 98 BATTERY STREET
    uppercase("")  # (prints just newline)
    uppercase("z")  :
