''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''

#if statement
integerNum1, integerNum2 = 9,6

if(integerNum1 > integerNum2):
    print("9 is greater than 6")

#if else statement

if(integerNum1 != integerNum2):
    print("TRUE")
else:
    print("FALSE")

#if...elif

number = 3

if(number == 1):
    print("Monday")
elif(number == 2):
    print("Tuesday")
elif(number ==3):
    print("Wednesday")
else:
    print("4 days remain")