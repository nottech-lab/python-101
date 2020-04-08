'''
TASK 5

We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked.

'''

#CODE

def is_leap(year):
    leap=False

    flag = year%400
    flag1 = year%4
    flag2 = year%100

    if(flag2== 0):
        m = year/100
        flag5 = m%4
        if(flag5 == 0):
            leap = True
        leap  = leap
    elif(flag == 0):
        leap == True
    elif (flag1 == 0):
        leap = True

    return leap


year = int(input())
if(is_leap(year)==False):
    print(year,"This is not a multiple of 4 hence it's not a leap year.")
else:
    print(year,"This is a multiple of 4 hence it's a leap year.")