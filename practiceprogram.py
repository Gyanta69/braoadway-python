#1.
'''
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")
'''
#2.Write a Python program to find out what version of Python you are using.
'''
import sys
print("Python Version is:")
print(sys.version)
print("Version Info:")
print(sys.version_info)
'''

#3 Write a Python program to display the current date and time.
'''
import datetime
x = datetime.datetime.now()
print("The current date and time : ")
print(x.strftime("%Y-%m-%d %H:%M:%S"))
'''
#4 Write a Python program that calculates the area of a circle based on the radius entered by the user.
'''
from math import pi
r = int(input("Enter the radius of the circle:"))

area = pi*r**2
print("The area of circle is:",area)
'''
#5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
'''
fName = str(input("Enter the first name :"))
lName = str(input("Enter the last name :"))
print(lName,fName)'''
#6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
'''
l = input("Enter the numbers:")
list = l.split(",")
tuple = tuple(list)
print("List:",list)
print("Tuple:",tuple)'''
#7.Write a Python program to display the first and last colors from the following list.
'''
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[3])
'''
#8.Write a Python program to display the examination schedule. (extract the date from exam_st_date).
'''
exam_st_date = (11, 12, 2014)
print(f'The exam will start from: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}')'''
#9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.Sample value of n is 5
'''
n = int(input("Enter a number :"))
print(n + n*n + n*n*n)
'''
#10.Write a Python program that prints the calendar for a given month and year.
'''
import calendar
year = int(input("Input the year:"))
month = int(input("Input the month:"))
print(calendar.month(year,month))
'''

