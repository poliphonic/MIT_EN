#!/usr/bin/env python3

# Write a Python function, odd, that takes in one number and returns
# True when the number is odd and False otherwise.
# You should use the % (mod) operator, not if.
# This function takes in one number and returns a boolean.


def odd(x):
    """
    x: int
    return: True if x is odd, False otherwise
    """
    return bool(x % 2)
