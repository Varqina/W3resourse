"""Write a Python program to sum all the items in a list."""
from Python37_win64.Lib import string
from Python37_win64.Lib.random import randint

import DataGenerator


def sum_list_print(list_of_ints):
    result = 0
    for element in list_of_ints:
        result += element
    # print(result)


test_list = [1, 2, 3, 3, 3, 4, 5]
sum_list_print(test_list)

"""Write a Python program to get the largest number from a list."""


def find_highest_value_print(list_of_ints):
    highest_value = list_of_ints[0]
    for element in list_of_ints:
        if element > highest_value:
            highest_value = element
    # print(highest_value)


test_list = [1, 1, 2, 1, 55, 66, 77, 44, 33]
find_highest_value_print(test_list)

"""Write a Python program to count the number of strings where the string length is 2 or more and the first and last 
character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""


def get_count_for_task_int(list_of_strings):
    result = 0
    for element in list_of_strings:
        if len(element) >= 2 and element[0] == element[-1]:
            result += 1
    return result


test_list = ['abc', 'xyz', 'aba', '1221']
# print(get_count_for_task_int(test_list))

"""Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list
 of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""


def sort_by_second_tuple(tuple):
    return tuple[1]


def get_sorted_list(list_of_tuples):
    list_of_tuples.sort(key=sort_by_second_tuple)
    # print(list_of_tuples)


test_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
test_list.sort()
get_sorted_list(test_list)

"""Write a Python program to remove duplicates from a list."""


def remove_all_duplicates(list_of_elements):
    number_of_elements_in_list = 0
    result_list = []
    for element in list_of_elements:
        if result_list.count(element) == 0:
            result_list.append(element)
    if len(list_of_elements) == len(result_list):
        print("no duplicates")
    else:
        print("There was a duplicate")
    return result_list


test_list = [1, 2, 3, 1, 1, 'ala', 'lala', 'ala']

"""Write a Python program to clone or copy a list."""


def copy_list():
    list = DataGenerator.generate_testing_list(True)
    list2 = []
    for element in list:
        list2.append(element)


"""Write a Python program to print the numbers of a specified list after removing even numbers from it."""


def remove_even_number_and_reutrn_index():
    list = DataGenerator.generate_testing_list(True)
    removed_position_of_number_list = []
    not_even_list = []
    element_number = 0
    for element in list:
        if element % 2 == 0:
            removed_position_of_number_list.append(element_number)
        else:
            not_even_list.append(element)
        element_number += 1
    del list
    print(not_even_list)
    print(removed_position_of_number_list)


"""Write a Python program to insert an element before each element of a list."""


def insert_int_before_each_element():
    temporary_list = DataGenerator.generate_testing_list(True)
    result_list = []
    print(temporary_list)
    for element in temporary_list:
        result_list.append(DataGenerator.generate_random_int(8))
        result_list.append(element)
    if len(temporary_list) * 2 != len(result_list):
        print("error")
    print(result_list)


"""Write a Python program to print a list of space-separated elements"""


def look_for_empty_character_in_string(string_element, result_list):
    if isinstance(string_element, str) and string_element.find(" ") > 0:
        result_list.append(string_element)


def look_for_empty_character_in_list(element, result_list):
    if isinstance(element, list):
        for value in element:
            run_search_for_empty_character(value, result_list)


def look_for_empty_character_in_dictionary(element, result_list):
    """check if it is other coercion and invoke remaining things"""
    pass


def look_for_empty_character_in_tuple(element, result_list):
    if isinstance(element, tuple):
        element = list(element)
        look_for_empty_character_in_list(element,result_list)


def run_search_for_empty_character(object_element, result_list):
    for element in object_element:
        look_for_empty_character_in_string(element, result_list)
        look_for_empty_character_in_list(element, result_list)
        look_for_empty_character_in_dictionary(element, result_list)
        look_for_empty_character_in_tuple(element, result_list)


def look_for_empty_character_in_collection(collection_element, result_list):
    if isinstance(collection_element, list) or isinstance(collection_element, dict) \
            or isinstance(collection_element, tuple) or isinstance(collection_element, dict):
        run_search_for_empty_character(collection_element, result_list)


def return_list_of_elements_with_space():
    testing_list = DataGenerator.generate_testing_list(True, True, True, True)
    result_list = []
    print(testing_list)
    for element in testing_list:
        look_for_empty_character_in_string(element, result_list)
        look_for_empty_character_in_collection(element, result_list)
    print(result_list)


"""Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply 
the numbers by 5. Print the unique numbers in ascending order separated by space. """


def print_max_and_min():
    testing_list = DataGenerator.generate_testing_list(True)
    max_int = None
    min_int = None
    result_tab = []
    for element in testing_list:
        if isinstance(element, int):
            if max_int is None or element > max_int:
                max_int = element
            if min_int is None or element < min_int:
                min_int = element
            if result_tab.count(element) == 0:
                result_tab.append(element)
    result_tab.sort()
    print(result_tab)
    print(max_int)
    print(min_int)


print_max_and_min()
