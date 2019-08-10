'''
Write a simple script that would take input from user using keyboard 
'''

# python allow user to interact with a program by allowing them to enter values for variables through keyboard
# input() function does the magic of allowing the user to insert data into a program

student_name = input("Please enter your name: ")
# This will enable user to set a string value for a variable student_name

student_age = eval(input("Please enter your age: "))
# This will enable user to set an evaluated value to an age variable which can later be used as a part of mathematical calculation

student_DOB = int(input("Please enter year you were born: "))

age = 2019 - student_DOB

if student_age == age:
    print("Thanks {student} for your honest. You are {age} years old".format(student = student_name, age = student_age))
else:
    print("You are not telling the truth {student_name} the age doesnt match with year you were born".format(student_name = student_name))    
