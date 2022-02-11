#!/usr/bin/env python3

# Write a procedure called oddTuples, which takes a tuple as input, and
# returns a new tuple as output, where every other element of the input
# tuple is copied, starting with the first one. So if test is the tuple
# ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this
# input would return the tuple ('I', 'a', 'tuple').


def odd_tuples(a_tup):
    """
    a_tup: a tuple
    return: tuple, every other element of a_tup
    """
    return a_tup[::2]
