'''
Write a simple script that demonstrate your understanding of functions in python 
'''
# TO DEMOSTRATE PYTHON FUNCTIONS WE ARE GOING TO SOLVE FOLLOWING PROBLEM
"""
TASK
    We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
    In the Gregorian calendar three criteria must be taken into account to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
    The year is also evenly divisible by 400. Then it is a leap year.
    This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

REQUIRED 
    You are given the year, and you have to write a function to check if the year is leap or not.
    Note that you have to complete the function and remaining code is given as template.

INPUT FORMAT
    Read y, the year that needs to be checked.

CONSTRAINTS
    1900 <= y <= 10^5

OUTPUT FORMAT

    Output is taken care of by the template. Your function must return a boolean value (True/False)

SAMPLE INPUT 0
    1990

SAMPLE OUTPUT 0
    False

EXPLANATION 0
    1990 is not a multiple of 4 hence it's not a leap year.
"""
# Function Definiton, while defining a function it is advised to to use a name conversion like python variables
# A function name should start with either a letter or an underscore followed by alphanumeric characters 
# A function name can not start with number or any of the special characters such as period
# In python it is adviced to follow camelCase style while naming functions i.e. The first word should start with lowercase and for any following word, should start with uppercase
# See the example below
#   
def isLeapYear():
    year = int(input("Please enter a year: "))

    # Checking if a year is within acceptable input range
    if year >= 1900 and year <= (10 ** 5):
        # This section checks if a given year is a leap year or not
        if (year % 4 == 0 and year % 400 == 0):
            return True 
        elif year % 4 == 0 and year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True           
    else:
        print("{} is not within a range, please choose a year between 1900 and 100000".format(year))
        return False     

# Function Calling
if isLeapYear():
    print("This is a leap year")
else:
    print("This is not a leap year")       

print()
# In Python function can accept parameters or cannot
# PARAMETERS are defined as variables that are used to pass values to a function for further manipulation
# Function can accept any number of parameters as it will be demostrated below
# Above is an example of a function which does not accept any of the parameters
# Below is an example of a function that accept a certain number of parameters 

# Function definition
def personalDetails(firstname,lastname,age):
    print("My name is {firstname} {lastname} and am {age} years old".format(firstname=firstname,lastname=lastname,age=age))

# Calling a function with arguments
personalDetails("Issa", "Juma", 24)

# Python supports functions with default parameters, see the example below
def average(item1 = 1, item2 = 1, item3 = 1):
    average = (item1 + item2 + item3) / 3
    return average
    
# When we call the function average() we can decide either to pass an arguments or not
# If we pass an arguments the function will calculate the average based on the given arguments
# But if we call a function without any arguments the function will calculate the average using default values assigned to the parameters during function definition
# DEMO

print()
print("Without passing arguments the average is {}".format(average()))
print("With arguments the average is {}".format(average(2,3,4)))
   
