'''
Python list is a data structure a mutable data structure acts as a container that holds other objects in a given order.
Data in a python list can be of different type or of the same type separated by comma, stored in index basis.
Python list is created by enclosing the data in a square brackets [], where each element is separated by a comma
Syntax:
    listname = [elem1,elem2,elem3,.........,elemN]
Elements in a list can be accessed using index either from the begining of the list or from trhe end of a list.       
'''

# Creating an empty list
item_list = []

# Adding data in a list
item_list = [1,2,3,4,5]

print(item_list) 

# List can store data of different type
student_info = ["Issa","Juma",24,"UDOM", "T/UDOM/2016/07975"]
print(student_info)

# Accessing data in a list via index
firstname = student_info[0]
lastname = student_info[1]
age = student_info[2]
university = student_info[3]
registration_number = student_info[4] 

print("my name is {fname} {lname}, am {age} years old. {reg} is my registration number at {univ}".format(fname = firstname, lname = lastname, age = age, reg=registration_number, univ = university))
print()

# Iteration in a list
for item in student_info:
    print(item)
print()

# Python list can be added together to create another giant list
gigantic_list = item_list + student_info
print(gigantic_list)

# List can be replicated up to multiple times
print(student_info * 2)

# We can slice a list just like slicing a string
print(student_info[:3])
print(student_info[1:4])
print(student_info[2:])


# Updating a list, this allow to change values of a list items
student_info[0] = "Joshua"
print(student_info)

# Appending a list
student_info.append("Block one")
print(student_info)

# List items can be deleted via a del()
del(student_info[2:])
print(student_info)

# Finding minimum and maximum
minimum = min(item_list)
maximum = max(item_list)
length = len(item_list)
print("The minimum item in {lixt} is {minimum} and the maximum item is {maximum} while the length of a list is {length}".format(lixt = item_list, minimum = minimum, maximum = maximum, length = length))  