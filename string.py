'''
Write a simple script to demonstrate your understanding of strings 
'''
#Accessing values in strings:
string1 = "Spies In Disguise"
string2 = "Is Nice"
print(string1[2])

#Updating strings:
string2 ="Is Nice"
print(string2[:4] + "Awesome")

#String Special Operators:
string1 = "Spies In Disguise"
string2 = "Is Nice"
#string concatenation
print(string1 + string2)

#repetation
print(string2*2)

#slice
string1 = "Spies in disguise"
print(string1[3])

#range slice
string1 = "Spies in disguise"
print(string1[2:6])

#the 'in' membership
string1 = "Spies in disguise"
print("d" in string1)

#the 'not in' membership
string1 = "Spies in disguise"
print("z" not in string1)


#String Formatting Operator:
name = "Freya"
age = 18
print("%s is %d years old." %(name, age))


#Built In String Method:
string1 = "spies In Disguise"
string2 = "Is Nice"
#Capitalize
print(string1.capitalize)

#Uppercase
print(string2.upper())

#Replace
print(string1.replace("In", "On"))

#len:gives no of items in a string
print(len(string1))


