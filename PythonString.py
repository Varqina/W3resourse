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