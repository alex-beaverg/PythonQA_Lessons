# Homework 09, file 1 (2023.06.12)
# Classwork

import time


# TODO: Homework:

# TODO: Actions with list()
# TODO: Actions with tuple()
# TODO: Actions with dict()
# TODO: My own container() and actions with it

class MyContainer:
    def __init__(self):
        self.items = ['Mother', 'Father']

    def __contains__(self, item):
        return item in self.items


def work_with_containers(first, second):
    print()
    simple_container = [1, 2, 3]
    if first in simple_container:
        print(f"This element ({first}) is placed in container")
    if second not in simple_container:
        print(f"This element ({second}) isn't placed in container")
    print()

    first_empty_list = list()
    second_empty_list = []
    first_list = [1, "second", 3.5, list()]
    second_list = list(i for i in range(3))
    print(first_empty_list)
    print(second_empty_list)
    print(first_list)
    print(second_list)
    first_list[0] = 25
    first_list[1] = 125
    first_list[3] = 225
    print(first_list)
    # first_list[4] = 325   # IndexError
    # print(first_list)
    print()

    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    del my_list[0]
    print(my_list)
    del my_list[:2]
    print(my_list)
    del my_list[:]
    print(my_list)
    print()

    a = [3, 2, 1]
    b = [1, 2, 3]
    d = [3, 2, 2]
    e = [3, 2]
    f = [3, 2, 'a']
    print(a > b)  # True
    print(a > d)  # False
    print(d > b)  # True
    print(a > e)  # True
    # print(a > f)    # TypeError
    print()

    print(my_list)
    my_list.append(1)
    print(my_list)
    my_list.append(2)
    print(my_list)
    my_list.append(3)
    print(my_list)
    my_list.append(4)
    print(my_list)
    my_list.append(5)
    print(my_list)
    print()

    start1 = time.time()
    some_my_list = list()
    for i in range(100_000_000):
        some_my_list.append(i)
    delta1 = round(time.time() - start1, 3)
    print(f"Length of some_my_list = {len(some_my_list)}, time = {delta1} seconds")

    start2 = time.time()
    strange_list = list(i for i in range(100_000_000))
    delta2 = round(time.time() - start2, 3)
    print(f"Length of strange_list = {len(strange_list)}, time = {delta2} seconds")
    print()

    some_list = [1, 3, 8, 7]
    print(some_list[-1])
    print(some_list[-3])
    print(some_list[4::-1])
    print()

    another_list = list(range(2, 10, 2))
    print(another_list)
    negative_list = list(range(2, -10, -2))
    print(negative_list)
    print()

    value_index = negative_list.index(-6, 0, 5)
    print(value_index)
    print()

    first_tuple = tuple()
    second_tuple = tuple('abc')
    third_tuple = tuple([1, 2, 3])
    range_tuple = tuple(range(5))
    list_tuple = tuple(another_list)
    print(first_tuple)
    print(second_tuple)
    print(third_tuple)
    print(range_tuple)
    print(list_tuple)
    print()

    print(second_tuple[1])
    # second_tuple[1] = 'd'     # TypeError

    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict)
    print(my_dict.items())
    print(my_dict.values())
    print(my_dict.keys())
    print(list(my_dict.items())[0])
    print()

    family = MyContainer()
    print('Father' in family)
    print('Mother' in family)
    print('Lover' in family)

    if 'Father' and 'Mother' in family:
        print('Happy childhood!')


if __name__ == "__main__":
    work_with_containers(2, 4)
