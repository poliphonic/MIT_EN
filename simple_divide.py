#!/usr/bin/env python3

# Suppose we rewrite the fancy_divide function to use a helper function.
# Your task is to change the definition of simple_divide so that the
# call does not raise an exception. When dividing by 0, fancy_divide
# should return a list with all 0 elements. Any other error cases should
# still raise exceptions. You should only handle the ZeroDivisionError.


def fancy_divide(list_of_numbers, index):
    """
    list_of_numbers: list of numbers
    index: an integer
    return: list of changed numbers
    """
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    """
    item: a number
    denom: a number
    return: return item / denom if denom != 0 else 0
    """
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


print(fancy_divide([0, 2, 4], 0))
