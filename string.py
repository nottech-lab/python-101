'''
Write a simple script to demonstrate your understanding of strings 
'''

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
