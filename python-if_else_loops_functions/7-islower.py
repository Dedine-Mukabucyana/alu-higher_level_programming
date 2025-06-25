#!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase without using string methods or imports."""
    if not isinstance(c, str) or len(c) != 1:
        return False
    return ord('a') <= ord(c) <= ord('z')

# Test cases
if __name__ == "__main__":
    test_cases = ["", "a", "H", "4", "I", 4]
    for case in test_cases:
        status = "lower" if islower(case) else "upper"
        print(f"{case} is {status}")
