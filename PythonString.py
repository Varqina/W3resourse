"""Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""


def count_letter_frequency_dictionary(input_string):
    result_dictionary = {}
    while len(input_string) != 0:
        result_dictionary[input_string[0]] = input_string.count(input_string[0])
        input_string = input_string.replace(input_string[0], "")
    return result_dictionary


print(count_letter_frequency_dictionary("www.google.com"))

"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string 
length is less than 2, return instead of the empty string."""


def create_string_from_prefix_and_suffix(input_string):
    input_string = input_string.replace(" ", "")
    if len(input_string) >= 2:
        return input_string[0] + input_string[1] + input_string[-2] + input_string[-1]
    else:
        return ""


def is_test_create_string_from_prefix_and_suffix(input_string, expected_string):
    return True if create_string_from_prefix_and_suffix(input_string) == expected_string else False


print(is_test_create_string_from_prefix_and_suffix('w3resource', 'w3ce'))
print(is_test_create_string_from_prefix_and_suffix('w3', 'w3w3'))
print(is_test_create_string_from_prefix_and_suffix(' w', ""))

"""Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'"""


def change_all_characters_by_first_expect_first_string(input_string):
    first_character = input_string[0]
    input_string = input_string.replace(first_character,"$")
    print(first_character + input_string[1:])

change_all_characters_by_first_expect_first_string("restart")