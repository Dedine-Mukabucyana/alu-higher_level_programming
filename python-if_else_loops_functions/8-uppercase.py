#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase without using str.upper()."""
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)


if __name__ == "__main__":
    uppercase("holberton")  # HOLBERTON
    uppercase("Holberton School")  # HOLBERTON SCHOOL
    uppercase("Holberton School, 98 battery street")  # HOLBERTON SCHOOL, 98 BATTERY STREET
    uppercase("")  
