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
import sys

from Python37_win64.Lib import os


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
task2()