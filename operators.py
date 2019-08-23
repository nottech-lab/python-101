'''
Write a simple script that demonstrate your understanding of Operators,operands and operator precedence
'''

#additional of two numbers
x= 4	
y= 5
print(x + y)

#comparison of two numbers
x = 4
y = 5
print(('x > y  is',x>y))
#compound assignment operator
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print(("Line 1 - Result of + is ", res))
#logical operators
a = True
b = False
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))
#membership operator
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")