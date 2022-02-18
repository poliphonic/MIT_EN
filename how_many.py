#!/usr/bin/env python3

# We want to write some simple procedures that work on dictionaries to
# return information.
# Write a procedure, called how_many, which returns the sum of the
# number of values associated with a dictionary.


def how_many(a_dict):
    """
    a_dict: a dictionary, where all the values are lists
    return: int, how many values are in the dictionary
    """
    res = 0
    for i in a_dict.keys():
        res += len(a_dict[i])
    return res


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
print(how_many(animals))
