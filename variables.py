'''
Write a simple script to demonstrate your understanding of Variable,identifier and keywords
'''
             # VARIABLES.
# Variable is a container for storing different types of data values.
# The type of variable depend on the type of data that you are going to store.
# Integer, float,hexadecimal and long are under category of numbers data type. 
# String  variables are enclosed by characters in quotes of which can either be single, double or triple quotes.
# List variables are used to store values of list datatype.
# Tuple variable is used to store values which are fixed in size, elements once inserted can not be removed.
# Dictionary variable is used to hold a lot of related informations which is the list of "key" and "values" pair separated by comma.
# Set variable is used to store values of set datatype.

            # 1. NUMBERS
# It can be integer, float, hexadecimal or long.
            
            # INTEGER.
x = 4
print(x)
type(x) # The variable x is of type int.

            # FLOAT.
# Float variable store values or data that are in form of decimal points.
z = 4.12345
print(z)
type(z)

            # 2. STRING.
# Can be declared either by single or double quotes.
y = "Daudi"
# Which is the same as
y = 'daudi'
print(y)
type(y) # The variable y is of type str.



            # 3. LIST.
 # Data type that is used to store a list or collection values.
 # IS the collection which is ordered and changeable.
 # It allows data duplication.
This_list = ["Daudi", "Juma", "John"]
print(This_list)
type(This_list) # The variable This_list is of type list.

            # 4. TUPLE.
# Is the collection which is ordered and unchangeable.
# Tuples in python is writen in round brackets.
This_tuple = ("Avocado", "Banana", "Apple")
print(This_tuple)
type(This_tuple) # The variable This_tuple is of type tuple.

            # 5. DICTIONARY.
# Is the collection which is ordered, changeable and indexed.
# Dictionaries are writen in curly  brackets.
# They have keys and values.
# Values can be extracted by the key name
This_dict = {"Name": 'Daudi', "Date of birth": 19, "Year": 1997}
print(This_dict)
type(This_dict) # The variable This_dict is of type dict.

            # 6. SET.
# Is the collection which is ordered and unindexed.
# In python sets are writen in curly brackets.
This_set = {"Avocado", "Banana","Apple"}
print(This_set)
type(This_set) # The variable This_set is of type set.

            # Assigning values to multiple variables.
# Python allows to assign values to multiple variables.
a, b, c = "Avocado", "Banana", "Apple"
print(a)
print(b)
print(c)
# Python allows to store tha same value in multiple variable.
a = b = c = "Avocado"
print(a)
print(b)
print(c)
