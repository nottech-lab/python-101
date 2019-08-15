'''
Write a simple script that demonstrate your understanding of Operators,operands and operator precedence
'''
#Basic operators

x , y , z = 1, 2, 0
# Python Arithmetic Operators
z = x + y       #Addition 
print('Sum is:', z)

z = y - x    #Subtraction
print('Difference is:', z)

z= x * y   #Multiplication
print('Product is:', z)

z = y / x    #Division
print('Quotation is:', z)

z = y % x    #Module
print('Module is:', z)

x , y , z = 10 , 2 , 0
z = x**y    #Exponent
print('Exponent of x to y is:', z)

z = x // y   #Floor division
print('Z is:', z)

#Python Comparison Operators

if x >= y:                #If values not equal prints true similar to != 
     print('x is equal to y')
else:
     print('x is not equal to y')

#Python Assignment Operators

z += x            #Adds right oparand to left operand and assign results to left operand i.e z = z + x
z -= y            #Subtracts right oparand to left operand and assign results to left operand i.e z = z - y
z **= x           #Perform exponential and assign the value to left operand i.e z = z**x

#Python Bitwise Operators

x , y , z = 40, 20, 0
z = x & y             #AND
print('x AND y is:', z)

z = x | y             #OR
print('x OR y is', z)

z = x ^ y             #XOR
print('x XOR y is:', z)

#Python Membership Operators
x  = 10
list_ = [1, 2, 3, 5]
if x in list_:
    print('x is found in list')
elif x not in list_:
    print('x is not found in list')
else:
    print('Choose again')

#Python Identity Operators
x, y = 10, 20
if id(x) is id(y):
    print('x is equal to y')    
elif id(x) is not id(y):
    print('x is not equal to y')
else:
    print('Nothing to show')                



