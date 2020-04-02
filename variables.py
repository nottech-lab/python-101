'''
Write a simple script to demonstrate your understanding of Variable,identifier and keywords
'''

# This is a variable 

number1 = 55

print("number1 is a variable")

# Identifier starts with alphabet or underscore

string = "abc"
boolone = string[0].isnumeric()

if(boolone == True):
	print("This is not a valid identifier")
elif(boolone == False):
	print("This is a valid identifier")
elif(string[0] == _):
	print("This is a valid identifier")
else:
	print("Undefined")
	
	
#Key words in Python alread used above

True, False, None