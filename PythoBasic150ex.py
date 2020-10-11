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
#print(task1(sString))


"""Write a Python program to get the Python version you are using. Go to the editor"""
def task2():
    print("Python Version: " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro))
    os.system("python --version")
#task2()

"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""
def task3():
    now = datetime.datetime.now()
    ownTime = str(now.year) + "-" + str(now.month)+"-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
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
    return float((math.pow(r,2))*math.pi)

print(task4(1.1))

""" Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them."""
def task5(name, surname):
    finalName=""
    for letter in surname+name:
        finalName+=letter+" "
    print(finalName)

task5("Piotr", "Flis")


