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

"""Write a Python program to get a string from a given string where all occurrences of its first char have been changed 
to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'"""


def change_all_characters_by_first_expect_first_string(input_string):
    first_character = input_string[0]
    input_string = input_string.replace(first_character, "$")
    print(first_character + input_string[1:])


change_all_characters_by_first_expect_first_string("restart")

"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two
 characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""


def concatenate_strings_and_change_place_two_first_characters(input_1_string, input_2_string):
    input_1_constans_string = input_1_string
    input_1_string = input_2_string[0] + input_2_string[1] + input_1_string[2:]
    input_2_string = input_1_constans_string[0] + input_1_constans_string[1] + input_2_string[2:]
    print(input_1_string + input_2_string)


concatenate_strings_and_change_place_two_first_characters("abc", "xyz")

"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
 already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave 
 it unchanged
 Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""


def change_string_according_to_conditions_string(input_string):
    string_length = len(input_string)
    if string_length < 3:
        return input_string
    if input_string[string_length - 3:] == "ing":
        return input_string + "ly"
    else:
        return input_string + "ing"


print(change_string_according_to_conditions_string('abc'))
print(change_string_according_to_conditions_string('string'))

"""Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' 
follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the
 editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'"""


def make_string_positive_string(input_string):
    if input_string.find("not"):
        return input_string[0:input_string.index("not")] + "good" + input_string[input_string.find("poor") + 4:]
    else:
        return input_string.replace('poor', 'good')


print(make_string_positive_string('The lyrics is not that poor!'))

"""Write a Python function that takes a list of words and returns the length of the longest one."""


def return_longest_string_from_list(input_list_of_strings):
    highest_index_int = 0
    highest_value_int = 0
    for i in range(len(input_list_of_strings)):
        if len(input_list_of_strings[i]) > highest_value_int:
            highest_index_int = i
    return input_list_of_strings[highest_index_int]


string_list = ["aaaa", "vvvvvvv", "ccccccccccccccc"]
print(return_longest_string_from_list(string_list))

"""Write a Python program to remove the nth index character from a nonempty string"""


def remove_n_character_from_string(character_to_be_removed, input_string):
    return input_string.replace(character_to_be_removed, "")


print(remove_n_character_from_string("e", "test"))


"""Write a Python program to change a given string to a new string where the first and last chars have been 
exchanged. """


def change_first_and_last_character_of_string(input_string):
    return input_string[-1]+input_string[1:-2]+input_string[0]

print(change_first_and_last_character_of_string("aaaaaaabbbbbbb"))
