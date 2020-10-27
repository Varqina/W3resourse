from Python37_win64.Lib import string
from Python37_win64.Lib.random import randint


def generate_random_string():
    string_length = randint(1, 60)
    result_string = ""
    while string_length > len(result_string):
        result_string += string.printable[randint(0,len(string.printable)-1)]
    return result_string


def generate_random_list(depth=0):
    """depth parameter is used to avoid recursion depth error"""
    if depth != 0:
        list_length = randint(1, depth)
    else:
        list_length = randint(1, 30)
    temporary_tuple_list = []
    while list_length > len(temporary_tuple_list):
        random_int_value = randint(0, 4)
        if random_int_value == 0: temporary_tuple_list.append(randint(0, 100))
        if random_int_value == 1: temporary_tuple_list.append(string.printable
                                                           [randint(0, len(string.printable) - 1)])
        if random_int_value == 2: temporary_tuple_list.append(generate_random_tuple(2))
        # if random_int_value == 3: add dictionary
        # if random_int_value == 4: add list
    return temporary_tuple_list


def generate_random_dictionary():
    """depth parameter is used to avoid recursion depth error"""
    pass


def generate_random_tuple(depth=0):
    """depth parameter is used to avoid recursion depth error"""
    return tuple(generate_random_list(depth))


def generate_testing_list(ints=False, strings=False, tuples=False, dictionaries=False, lists=False):
    testing_list = []
    list_length = randint(5, 20)
    while list_length > len(testing_list):
        if ints: testing_list.append(randint(0, 100))
        if strings: testing_list.append(generate_random_string())
        if tuples: testing_list.append(generate_random_tuple())
        if dictionaries: testing_list.append(generate_random_dictionary())
        if lists: testing_list.append(generate_random_list())

    return testing_list

for i in range(1):
    print(str(i) + " " + str(generate_testing_list(ints=True, strings= True, tuples=True, dictionaries=True, lists=True)))


