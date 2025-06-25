#!/usr/bin/python3
if __name__ == "__main__":
    import marshal
    import sys

    # Read .pyc file (skip header, which is 16 bytes in Python 3.7+)
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # skip magic number, timestamp, and hash
        code = marshal.load(f)

    # code.co_names contains names defined in the bytecode
    names = [name for name in code.co_names if not name.startswith("__")]

    for name in sorted(names):
        print(name)
