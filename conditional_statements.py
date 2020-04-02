''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''
num = 4

#if

if(num > 0):
	print("This is Positive number")
	
#if else

if(num > 0):
	print("This is Positive Number")
else:
	print("This is Negative number")
	
#elif

num1 = 3
num2 = 5


if(num1 > num2):
	print(num1,"Is greater than ",num2)
elif(num1 < num2):
	print(num1,"Is less than ",num2)
else:
	print(num1," and ",num2, "are equal")
