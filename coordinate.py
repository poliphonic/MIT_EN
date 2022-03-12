#!/usr/bin/env python3

# Your task is to define the following two methods for the Coordinate
# class:
# Add an __eq__ method that returns True if coordinates refer to same
# point in the plane (i.e., have the same x and y coordinate).
# Define __repr__, a special method that returns a string that looks
# like a valid Python expression that could be used to recreate an
# object with the same value. In other words, eval(repr(c)) == c given
# the definition of __eq__ from part 1.


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        """
        getter method for a Coordinate object's x coordinate
        """
        return self.x

    def get_y(self):
        """
        getter method for a Coordinate object's y coordinate
        """
        return self.y

    def __str__(self):
        return f'<{self.get_x()}, {self.get_y()}>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Coordinate({self.x}, {self.y})'
