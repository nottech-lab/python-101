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

#VARIABLES AND THEIR DATA TYPES
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

#********** STRING ***********
top()
print("\t\tSTRINGS")
print()

#String is a built-in type text sequence, used to handle textual data
#Created by enclosing a text in a single or double quotes
#The benefit of using string is that it can be accessed using indexes as in python list
#Example consider a program that print a string in a reverse order

lab = 'NOTTECH'
length = len(lab)
iterator = length - 1

print("\tNormal \t\t Reverse")
print()
for i in range(length):
	j = -length + iterator
	print("\t{normal} \t\t {reverse}".format(normal=lab[i], reverse=lab[j]))
	iterator -= 1
#The code above make use of string stored in a variable called "lab"
#len() function is used to get length of a string as illustrated in line 100
#Python provide a lot more built-in methods to perform different string operation
#STRING OPERATORS
	#1) Basic Operators (*, +), used for string replication and concatenation respectively
	#2) Membership Operator (in, not in)
	#3) Relational Operator (<, >, <=, >=, ==, !=, <>), used to compare strings
#EXAMPLES
print("\t\tSTRINGS OPERATORS")
print()

studentOne = 'ISSA'
studentTwo = 'DJEKO'
studentThree = "ISSA JUMA"

print("\tReplicated string: " + 2 * studentOne)
print("\tString concatenation: " + studentOne + " " + studentTwo)
print("\tIs studentOne string not a member of studentTwo string? => " +
      str(studentOne not in studentTwo))
print("\tIs studentOne string a member of studentThree string? => " +
      str(studentOne in studentThree))
print("\tIs a studentOne equal to studentThree? => " +
      str(studentOne == studentThree))

#********** LIST ***********
top()
print("\t\tLIST")
print()
#List in python is like an array in other programming language with exception list can store data of different type
#Below is a program that find sum of digits in a number by making a use of list
number = 323
digits = []  # This creates an empty list called "digits"
# This converts a number into an equivalent string and store the result in a "temp_string" variable
temp_string = str(number)

for i in range(len(temp_string)):
	# This line access each digit in a string, convert it into an integer and lastly insert into a list
	digits.append(int(temp_string[i]))

print("The sum of digits in 323 is: {}".format(sum(digits)))

#********** Tuple ***********
top()
print("\t\tTUPLES")
print()
#Python tuples are much like list except they are created using blackets instead of square brackets as list
#Another difference with a list is that tuples are immutable i.e. u cannot change data once in a tuple
#Example

developers = ("Tajr", 201, "Faith", 201.9, "Wikedz", 200)
print(developers)

#********** Dictionary ***********
top()
print("\t\tDICTIONARY")
print()
#Python Dictionaries are an unordered set of key and value
#Declared using curly brackets in python
#Example
developer = {'Name': 'Tajr', 'Occupation': 'Developer', 'Experience Rate': 201}
print(developer)


bottom()