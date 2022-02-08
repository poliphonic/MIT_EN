#!/usr/bin/env python3

# The greatest common divisor of two positive integers is the largest
# integer that divides each of them without remainder. A clever
# mathematical trick (due to Euclid) makes it easy to find greatest
# common divisors. Suppose that a and b are two positive integers.
# Write a function gcd_recur(a, b) that implements this idea
# recursively. This function takes in two positive integers and returns
# one integer.


def gcd_recur(a, b):
    """
    a, b: positive integers
    return: the greatest common divisor of a and b
    """
    a, b = (a, b) if a > b else (b, a)
    return gcd_recur(a % b, b) if a % b else b
