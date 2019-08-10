"""
    VARIABLES
        => defines as memory location used to store data for a future use in a program
        => in python there are number of operations invoved when working with variables
            1) 	Variable declaration and assignment
            2)  Variable multiple assignment
            3)	Variable deletion via del statement
        => As variables store data to be used in a program, data can be of different types as python support the following five data types 
            a)	Numbers
            b)	String
            c)	List
            d)	Tuple
            e)	Dictionary
    Examples are shown below
"""
# VARIABLE DECLARATION AND ASSIGNMENT
#Syntax => variable_name = value

firstName = "Issa"
lastName = "Juma"
age = "12"


def top():
	print(55 * '=')
	print()


def bottom():
	print()
	print(55 * '=')
	print()

#Above are three variables declared and initialized with value as it's shown
#To access variable data we use a function in python called print()
#Example


top()
print("\t\tVARIABLE ACCESSING")
print()
print('\tfirstName: {}'.format(firstName))
print('\tlastName: {}'.format(lastName))
print('\tage: {}'.format(age))


#VARIABLE MULTIPLE ASSIGNMENT
#This approach is useful when you have multiple variable initialized with the same value
#Example

number_one = number_two = number_three = 30

#Above defined three variables named number_one, number_two and number_three all initialized 30 as initial value
#Accessing variables

top()
print("\t\tMULTIPLE ASSIGNMENT")
print()
print('\tnumber_one: {}'.format(number_one))
print('\tnumber_two: {}'.format(number_two))
print('\tnumber_three: {}'.format(number_three))

#VARIABLE DELETION WITH del STATEMENT
#del statement is used to delete value stored in a variable
#Example
top()
print("\t\tVARIABLE DELETION")
print()
try:
	del number_one
	# This line will throw NameError Exception
	print('\tnumber_one: {}'.format(number_one))
except NameError:
	print("\tA variable number_one has been deleted")

#********** NUMBERS ***********
#Python variables are capable of storing numbers in variables that can be used in different program operation
#Example consider a program to find sum of two in a number
top()
print("\t\tNUMBERS")
print()

firstNumber = 12
secondNumber = 13

answer = firstNumber + secondNumber

print("\tThe sum is: {}".format(answer))
#Here three variables were created firstNumber and secondNumber store integers to be added together
#Variable named "answer" is used to store the sum of firstNumber and secondNumber as integer
bottom()