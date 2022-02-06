#!/usr/bin/env python3

# Write a Python function, eval_quadratic(a, b, c, x), that returns the
# value of the quadratic a * x ** 2 + b * x + c.
# This function takes in four numbers and returns a single number.


def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients
             of a quadratic equation
    x: numerical value at which to evaluate the quadratic
    return: value counted by the formula
    """
    return a * x ** 2 + b * x + c
