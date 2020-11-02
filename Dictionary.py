"""Write a Python script to sort (ascending and descending) a dictionary by value."""
import operator

import DataGenerator


def sort_asceding_and_descending_dictionary():
    dictionary_for_test = {0:10, 1:22, 2:1}
    temporary_list = []
    min = None
    key = None
    while len(dictionary_for_test) != 0:
        for element in dictionary_for_test:
            if min is None or dictionary_for_test[element] <= min:
                key = element
                min = dictionary_for_test[element]
        temporary_list.append(min)
        dictionary_for_test.pop(key)
        min = None
        key = None
    print(temporary_list)
    temporary_list.sort(reverse=True)
    print(temporary_list)


    sorted_d = sorted(dictionary_for_test.items(), key=operator.itemgetter(1))
    sorted_d = dict(sorted(dictionary_for_test.items(), key=operator.itemgetter(1), reverse=True))
sort_asceding_and_descending_dictionary()