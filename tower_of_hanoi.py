#!/usr/bin/env python3

# The Tower of Hanoi is a mathematical puzzle consisting of three rods
# and a number of disks of various diameters, which can slide onto any
# rod. The puzzle begins with the disks stacked on one rod in order of
# decreasing size, the smallest at the top, thus approximating a conical
# shape. The objective of the puzzle is to move the entire stack to the
# last rod, obeying the following rules:
#  - Only one disk may be moved at a time.
#  - Each move consists of taking the upper disk from one of the stacks
#        and placing it on top of another stack or on an empty rod.
#  - No disk may be placed on top of a disk that is smaller than it.
# With 3 disks, the puzzle can be solved in 7 moves. The minimal number
# of moves required to solve a Tower of Hanoi puzzle is 2 ** n − 1,
# where n is the number of disks.


def hanoi(number, first, second, third):
    if number:
        hanoi(number - 1, first, third, second)
        print(f'Move a disc from {first} to {third}.')
        hanoi(number - 1, second, first, third)


hanoi(3, 'first rod', 'second rod', 'third rod')
