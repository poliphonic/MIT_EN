#!/usr/bin/env python3

# Write a function recur_power(base, exp) which computes base ** exp by
# recursively calling itself to solve a smaller version of the same
# problem, and then multiplying the result by base to solve the initial
# problem.
# This function should take in two values - base can be a float or an
# integer; exp will be an integer >= 0. It should return one numerical
# value. Your code must be recursive - use of the ** operator or looping
# constructs is not allowed.


def recur_power(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: base ** exp
    """
    if not exp:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recur_power(base, exp - 1)
