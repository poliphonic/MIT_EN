#!/usr/bin/env python3

# Your task is to modify the code for integer_division so that any error
# does not occur.


def integer_division(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument
    return: integer, the integer division of x divided by a
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


print(integer_division(5, 3))
