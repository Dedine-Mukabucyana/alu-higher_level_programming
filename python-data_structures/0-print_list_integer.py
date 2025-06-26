#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if not isinstance(i, int):
            raise TypeError("All elements of the list must be integers")
        print("{:d}".format(i))
