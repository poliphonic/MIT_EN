#!/usr/bin/env python3


class Food:

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.calories

    def density(self):
        return self.get_value() / self.get_cost()

    def __str__(self):
        return f'{self.name}: <{self.value}, {self.calories}>'


def build_menu(names_list, values_list, calories_list):
    """
    names_list, values_list, calories_list: lists of same length
    names_list: a list of strings
    values_list and calories_list: lists of numbers
    return: list of Foods
    """
    menu = []
    for i in range(len(values_list)):
        menu.append(Food(names_list[i], values_list[i], calories_list[i]))
    return menu


def greedy(items, max_cost, key_function):
    """
    assumes items a list, max_cost >= 0, key_function maps elements of
    items to numbers
    """
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0
    for i in range(len(items_copy)):
        if total_cost + items_copy[i].get_cost() <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()
    return result, total_value


def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print(f'Total value of items taken {val}')
    for item in taken:
        print(f'   {item}')


def test_greedys(meal, max_units):
    print(f'Use greedy by value to allocate {max_units} calories')
    test_greedy(meal, max_units, Food.get_value)
    print(f'\nUse greedy by cost to allocate {max_units} calories')
    test_greedy(meal, max_units, lambda x: 1 / Food.get_cost(x))
    print(f'\nUse greedy by density to allocate {max_units} calories')
    test_greedy(meal, max_units, Food.density)


def max_val(to_consider, avail):
    """
    to_consider: list of items
    avail: a weight
    return: a tuple of the total value of a solution to 0 / 1 knapsack
        problem and the items of that solution
    """
    if not to_consider or not avail:
        result = (0, ())
    elif to_consider[0].get_cost() > avail:
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        val, to_take = max_val(to_consider[1:], avail - next_item.get_cost())
        val += next_item.get_value()
        without_val, without_to_take = max_val(to_consider[1:], avail)
        if val > without_val:
            result = (val, to_take + (next_item, ))
        else:
            result = (without_val, without_to_take)
    return result


def test_max_val(food, max_units, print_items=True):
    print(f'Use search tree to allocate {max_units} calories')
    val, taken = max_val(food, max_units)
    print(f'Total value of items taken {val}')
    if print_items:
        for item in taken:
            print(f'   {item}')


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = build_menu(names, values, calories)

test_greedys(foods, 750)
print()
test_max_val(foods, 750)
