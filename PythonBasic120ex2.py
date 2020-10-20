"""Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from
each other """
import random


def task1(data_list):
    """It compare unique values of data sets"""
    return True if (len(data_list) == len(set(data_list))) else False


print(task1([1, 5, 7, 9]))
print(task1([2, 4, 5, 5, 7, 9]))

"""Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly 
once. """


def print_all_possible_strings():
    char_list = ['a', 'e', 'i', 'o', 'u']
    factorial_int = count_factorial_int(len(char_list))
    result_set = generate_all_strings_from_list_set(factorial_int, char_list)
    print(transform_set_to_string(result_set))

def count_factorial_int(number_int):
    """Count factorial for number_int"""
    result = 1  # needs to be 1, when 0 result always 0
    for i in range(number_int):
        i += 1
        result = result * i
    return result


def generate_all_strings_from_list_set(factorial_int, char_list):
    """Generate all possible strings from provided characters and return as set"""
    result_set = set()
    while len(result_set) != factorial_int:
        random.shuffle(char_list)
        result_set.add(''.join(char_list))
    return result_set


def transform_set_to_string(value_set):
    """Transform set to string"""
    result_string = ""
    for i in value_set:
        result_string = result_string + str(i) + " "
    return result_string

print_all_possible_strings()

"""Write a Python program to remove and print every third number from a list of numbers until the list becomes empty."""

def task3(number_list):
    """If finished row, start from beginning"""
    help_value_int = 2
    while len(number_list) > 2:
        if len(number_list) > help_value_int:
            print(number_list)
            print(number_list[help_value_int])
            number_list.pop(help_value_int)
            help_value_int += 2

        else:
            help_value_int = 2
    print(number_list[1])
    print(number_list[0])

def task4(number_list):
    """Continue counting even row is finished"""

nums = [10,20,30,40,50,60,70,80,90]
task3(nums)