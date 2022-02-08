#!/usr/bin/env python3

# The greatest common divisor of two positive integers is the largest
# integer that divides each of them without remainder.
# Write an iterative function, gcd_iter(a, b), that implements this
# idea. One easy way to do this is to begin with a test value equal to
# the smaller of the two input arguments, and iteratively reduce this
# test value by 1 until you either reach a case where the test divides
# both a and b without remainder, or you reach 1.


def gcd_iter(a, b):
    """
    a, b: positive integers
    return: the greatest common divisor of a and b
    """
    a, b = (a, b) if a > b else (b, a)
    ans = 1
    for i in range(1, b + 1):
        ans = i if not a % i and not b % i else ans
    return ans
