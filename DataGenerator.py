from Python37_win64.Lib import string
from Python37_win64.Lib.random import randint


def generate_random_string():
    string_length = randint(1, 60)
    result_string = ""
    while string_length > len(result_string):
        result_string += string.printable[generate_random_int(len(string.printable) - 1)]
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
        if random_int_value == 0: temporary_tuple_list.append(generate_random_int())
        if random_int_value == 1: temporary_tuple_list.append(string.printable
                                                              [generate_random_int(len(string.printable) - 1)])
        if random_int_value == 2: temporary_tuple_list.append(generate_random_tuple(2))
        if random_int_value == 3: temporary_tuple_list.append(generate_random_dictionary(2))
        if random_int_value == 4: temporary_tuple_list.append(generate_random_list(2))
    return temporary_tuple_list


def generate_random_dictionary(depth=0):
    """depth parameter is used to avoid recursion depth error"""
    if depth != 0:
        dictionary_length = randint(1, depth)
    else:
        dictionary_length = randint(1, 30)
    temporary_dictionary = {}
    while dictionary_length > len(temporary_dictionary):
        temporary_dictionary[generate_random_int(100)] = generate_random_string()
        temporary_dictionary[generate_random_string()] = generate_random_int()
        temporary_dictionary[generate_random_string()] = generate_random_string()
        temporary_dictionary[generate_random_int(100)] = generate_random_int()
    return temporary_dictionary


def generate_random_int(range=60):
    """depth parameter is used to avoid recursion depth error"""
    return randint(1, range)


def generate_random_tuple(depth=0):
    """depth parameter is used to avoid recursion depth error"""
    return tuple(generate_random_list(depth))


def sort_list_random(e):
    return len(str(e)) + generate_random_int(200)


def generate_testing_list(ints=False, strings=False, tuples=False, dictionaries=False, lists=False):
    testing_list = []
    list_length = randint(5, 20)
    while list_length > len(testing_list):
        if ints: testing_list.append(randint(0, 100))
        if strings: testing_list.append(generate_random_string())
        if tuples: testing_list.append(generate_random_tuple())
        if dictionaries: testing_list.append(generate_random_dictionary())
        if lists: testing_list.append(generate_random_list())

    testing_list.sort(key=sort_list_random)
    return testing_list
