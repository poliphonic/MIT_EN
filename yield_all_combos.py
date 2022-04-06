#!/usr/bin/env python3

from random import randint


class Item:

    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f'<{self.name}, {self.value}, {self.weight}>'


def build_items():
    return [Item(n, v, w) for n, v, w in (('clock', 175, 10),
                                          ('painting', 90, 9),
                                          ('radio', 20, 4),
                                          ('vase', 50, 2),
                                          ('book', 10, 1),
                                          ('computer', 200, 20))]


def build_random_items(n):
    return [Item(i, 10 * randint(1, 10), randint(1, 10)) for i in range(n)]


def power_set(items):
    num = len(items)
    for i in range(2 ** num):
        combo = []
        for j in range(num):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yield_all_combos(items):
    """
    generates all combinations of n items into two bags, whereby each
        item is in one or zero bags
    yields a tuple, (bag1, bag2), where each bag is represented as a
        list of which item(s) are in each bag.
    """
    num = len(items)
    for i in range(3 ** num):
        bag1, bag2 = [], []
        for j in range(num):
            if not i // 3 ** j % 3:
                bag1.append(items[j].get_name())
            elif i // 3 ** j % 3 == 1:
                bag2.append(items[j].get_name())
        yield bag1, bag2


cnt = 0
for it in yield_all_combos(build_items()):
    cnt += 1
    print(cnt, list(it))
