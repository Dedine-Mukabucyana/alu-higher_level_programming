#!/usr/bin/python3


def islower(c):
    """Check if character is lowercase without string methods or imports."""
    if not isinstance(c, str) or len(c) != 1:
        raise ValueError("Input must be a single character")
    return ord('a') <= ord(c) <= ord('z')


if __name__ == "__main__":
    test_cases = ["a", "H", "4", "I", "", 4]
    for case in test_cases:
        try:
            print(f"{case} is {'lower' if islower(case) else 'upper'}")
        except ValueError:
            pass
