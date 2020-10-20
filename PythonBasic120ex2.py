"""Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from
each other """
import random


def task1(dataList):
    return True if (len(dataList) == len(set(dataList))) else False


print(task1([1, 5, 7, 9]))
print(task1([2, 4, 5, 5, 7, 9]))

"""Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly 
once. """


# Easy Solution
def task2():
    char_list = ['a', 'e', 'i', 'o', 'u']
    resultSet = {}
    resultNumber = 0
    resultString = ""
    for i in range(len(char_list)):
        i += 1
        resultNumber = resultNumber * i
    print(resultNumber)
    while len(resultSet) != resultNumber:
        resultSet.add(random.shuffle(char_list))


    for i in resultSet:
        resultString.join(i)
    print(resultSet)
    print(resultString)

task2()