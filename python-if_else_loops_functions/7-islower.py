#!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase without using string methods."""
    if len(c) == 0:  # Handle empty string case
        return False
    return ord('a') <= ord(c) <= ord('z')

# Test cases
if __name__ == "__main__":
    test_cases = ['', 'a', 'H', '4', 'I', 4]
    for case in test_cases:
        if isinstance(case, str):  # Only process string inputs
            result = "lower" if islower(case) else "upper"
            print(f"{case} is {result}")
        else:
            print(f"{case} is upper")  # Non-string inputs are not lowercase
