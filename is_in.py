#!/usr/bin/env python3

# We can use the idea of bisection search to determine if a character is
# in a string, so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character
# you're looking for (the "test character"). If they are the same, we
# are done - we've found the character we're looking for!
# If they're not the same, check if the test character is "smaller" than
# the middle character. If so, we need only consider the lower half of
# the string; otherwise, we only consider the upper half of the string.
# (Note that you can compare characters using Python's < function.)
# Implement the function is_in(char, a_str) which implements the above
# idea recursively to test if char is in a_str. char will be a single
# character and a_str will be a string that is in alphabetical order.
# The function should return a boolean value.
# As you design the function, think very carefully about what the base
# cases should be.


def is_in(char, a_str):
    """
    char: a single character
    a_str: an alphabetized string
    return: True if char is in a_str, False otherwise
    """
    middle = len(a_str) // 2
    if not a_str or len(a_str) == 1 and char != a_str:
        return False
    elif char == a_str[middle]:
        return True
    elif char > a_str[middle]:
        return is_in(char, a_str[middle:])
    elif char < a_str[middle]:
        return is_in(char, a_str[:middle])
