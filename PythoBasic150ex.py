import calendar
import math
import sys
from Python37_win64.Lib import os
import datetime

"""
Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are

"""


def task1(string):
    # if star, appeared make /n and \t
    string = string.replace("star,", "star,\n\t")
    # if are! appeared make /n and 2x \t
    string = string.replace("are!", "are!\n\t\t")
    # if high, appeared make /n and 2x \t
    string = string.replace("high,", "high,\n\t\t")
    # if sky. appeared make /n
    string = string.replace("sky.", "sky.\n")
    return string


sString = "Twinkle, twinkle, little star,How I wonder what you are!Up above the world so high,Like a diamond in the sky.Twinkle, twinkle, little star, How I wonder what you are"
# print(task1(sString))


"""Write a Python program to get the Python version you are using. Go to the editor"""


def task2():
    print("Python Version: " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(
        sys.version_info.micro))
    os.system("python --version")


# task2()

"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""


def task3():
    now = datetime.datetime.now()
    ownTime = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(
        now.minute) + ":" + str(now.second)
    print("Current date and time :\n" + now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Current date and time :\n" + ownTime)


task3()

"""
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""


def task4(r):
    return float((math.pow(r, 2)) * math.pi)


print(task4(1.1))

""" Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them."""


def task5(name, surname):
    finalName = ""
    for letter in surname + name:
        finalName += letter + " "
    print(finalName)


task5("Piotr", "Flis")

""" Own Task1 having name and surname make letters revesred"""


def own1(name, surname):
    result = ""
    for letter in reversed(name + surname):
        result += letter
    return result


print(own1("Radoslaw", "Flis"))

"""6 to do"""

"""Write a Python program to accept a filename from the user and print the extension of that."""


def task7(filename):
    extension = ""
    switch = 0
    for letter in filename:
        if switch == 1:  # needs to be here to avoid aditional dot in extension name
            extension += letter
        if letter == ".":
            switch = 1

    return extension


print(task7("test.java"))

"""Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]"""


def task8(colors):
    print(colors[0] + " " + colors[len(colors) - 1])
    print(colors[0] + " " + colors[-1])


colors = ["Red", "Green", "White", "Black"]
task8(colors)

"""Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014"""


def task9(examDate):
    iValueDay = str(examDate.__getitem__(0))
    iValueMonth = str(examDate.__getitem__(1))
    if int(iValueDay) < 10:
        iValueDay = "0" + iValueDay
    if int(iValueMonth) < 10:
        iValueMonth = "0" + iValueMonth
    print("The examination will start from : " + iValueDay + " / " + iValueMonth + " / " + str(examDate.__getitem__(2)))


exam_st_date = (2, 12, 2014)
task9(exam_st_date)

"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615"""


def task10(n):
    value = str(n)
    result = 0
    for i in range(1, 4):
        result = result + int(value)
        value += str(n)
    return result


def task10Own(n):
    result = 0
    for i in range(1, 4):
        result = result + n
        n = n * n
    return result


print(task10(5))

"""Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
 Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument."""


def task11(function):
    print(function.__doc__)


task11(abs)

"""Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. """


def task12(month, year):
    print(calendar.TextCalendar().formatmonth(year, month))


task12(10, 1991)

"""Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days """


def task14(date1, date2):
    delta = datetime.date(date2.__getitem__(0), date2.__getitem__(1), date2.__getitem__(2)) - datetime.date(
        date1.__getitem__(0), date1.__getitem__(1), date1.__getitem__(2))
    print(delta.days)


task14((2014, 7, 2), (2014, 7, 11))

"""Write a Python program to get the volume of a sphere with radius 6."""


def task15(radius):
    return ((4 * math.pi * radius ** 3) / 3)


print(task15(6))

"""Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference."""


def task16(value):
    result = 17 - value
    if result < 1:
        result = 2 * (abs(result))
    return result


print(task16(22))

"""Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum"""


def task17(value1, value2, value3):
    return 3 * (value1 + value2 + value3) if value1 == value2 and value2 == value3 else value1 + value2 + value3


print(task17(1, 2, 3))

"""Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged."""


def task18(sValue):
    return sValue if sValue[0] == "I" and sValue[1] == "s" else "Is" + sValue


print(task18("test"))

"""Write a Python program to get a string which is n (non-negative integer) copies of a given string."""


def task19(sString, iN):
    result = ""
    for i in range(iN):
        result += sString
    return result


print(task19("test", 5))

"""Write a Python program to find whether a given number (accept from the user) is even or odd, print out an 
appropriate message to the user. """


def task20(iNumber):
    return "even" if iNumber % 2 == 0 else "odd"


print(task20(20))

"""write a Python program to count the number 4 in a given list"""


def task21(lList):
    iCouner = 0
    for element in lList:
        if element == 4:
            iCouner += 1
    return iCouner


lListTest = (1, 2, 3, 4, 4, 4, 5, 4)
print(task21(lListTest))

"""Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2. """


def task22(sString, iN):
    result = ""
    if len(sString) < 2:
        return 10 * sString
    else:
        for i in range(iN):
            result += sString
        return result


print(task22("abc", 5))

"""Write a Python program to test whether a passed letter is a vowel or not."""


def task23(cCharacter):
    tvovelTuple = ('a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y')
    try:
        tvovelTuple.index(cCharacter)
        return True
    except ValueError:
        return False


print(task23('a'))

"""Write a Python program to check whether a specified value is contained in a group of values"""


def task24(iDigit, lList):
    for i in lList:
        if i == iDigit:
            return True
    return False


lista = [1, 2, 3, 4, 5]
print(task24(6, lista))

"""Write a Python program to create a histogram from a given list of integers."""


def task25(cCharacter, lLIst):
    for i in lLIst:
        print(cCharacter * i)


task25("@", lista)

"""Write a Python program to concatenate all elements in a list into a string and return it."""


def task26(lList):
    sString = ""
    for i in lList:
        sString = sString + str(i)
    return sString


print(task26(lista))

"""Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence"""


def task27(lLista2):
    lReturnList = []
    for i in lLista2:
        if i <= 237:
            if i % 2 == 0:
                lReturnList.append(i)
    print(lReturnList)

lTestList = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527]
task27(lTestList)

"""Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}"""

def task28():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(color_list_1-color_list_2)
    print(color_list_1.difference(color_list_2))

task28()

"""Write a Python program that will accept the base and height of a triangle and compute the area."""

def task29(fBase, fHeight):
    return 0.5 * fBase * fHeight

print(task29(1.222, 3.444))