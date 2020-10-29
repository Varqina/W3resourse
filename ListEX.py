"""Write a Python program to sum all the items in a list."""
from Python37_win64.Lib import string
from Python37_win64.Lib.random import randint

import DataGenerator


def sum_list_print(list_of_ints):
    result = 0
    for element in list_of_ints:
        result += element
    #print(result)


test_list = [1, 2, 3, 3, 3, 4, 5]
sum_list_print(test_list)

"""Write a Python program to get the largest number from a list."""


def find_highest_value_print(list_of_ints):
    highest_value = list_of_ints[0]
    for element in list_of_ints:
        if element > highest_value:
            highest_value = element
    #print(highest_value)


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
#print(get_count_for_task_int(test_list))

"""Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list
 of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""


def sort_by_second_tuple(tuple):
    return tuple[1]


def get_sorted_list(list_of_tuples):
    list_of_tuples.sort(key=sort_by_second_tuple)
    #print(list_of_tuples)


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

for i in range(0,5):
    DataGenerator.generate_testing_list(True)

