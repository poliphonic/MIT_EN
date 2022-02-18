#!/usr/bin/env python3

# We want to write some simple procedures that work on dictionaries to
# return information.
# This time, write a procedure, called biggest, which returns the key
# corresponding to the entry with the largest number of values
# associated with it. If there is more than one such entry, return any
# one of the matching keys.
# If there are no values in the dictionary, biggest should return None.


def biggest(a_dict):
    """
    a_dict: a dictionary, where all the values are lists
    return: the key with the largest number of values associated with it
    """
    key, val = 0, 0
    for i in a_dict:
        key, val = (i, len(a_dict[i])) if len(a_dict[i]) >= val else (key, val)
    return key if key else None


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],
           'd': ['donkey', 'dog', 'dingo']}
print(biggest(animals))
