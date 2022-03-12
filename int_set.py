#!/usr/bin/env python3

# Your task is to define the following two methods for the IntSet class:
# Define an intersect method that returns a new IntSet containing
# elements that appear in both sets.
# Add the appropriate method(s) so that len(s) returns the number of
# elements in s.


class IntSet:
    """
    an IntSet is a set of integers
    the value is represented by a list of ints, self.vals
    each int in the set occurs in self.vals exactly once
    """

    def __init__(self):
        """
        create an empty set of integers
        """
        self.vals = []

    def insert(self, element):
        """
        assumes element is an integer and inserts element into self
        """
        if element not in self.vals:
            self.vals.append(element)

    def member(self, element):
        """
        assumes element is an integer
        return: True if element is in self.vals, and False otherwise
        """
        return element in self.vals

    def remove(self, element):
        """
        assumes element is an integer and removes element from self.vals
        raises ValueError if element is not in self
        """
        try:
            self.vals.remove(element)
        except ValueError:
            raise ValueError(element, 'not found')

    def __str__(self):
        """
        return: a string representation of self
        """
        self.vals.sort()
        return '{' + ", ".join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """
        return: IntSet, containing elements those are in both sets
        """
        seq = IntSet()
        for item in self.vals:
            if item in other.vals:
                seq.insert(item)
        return seq

    def __len__(self):
        return len(self.vals)
