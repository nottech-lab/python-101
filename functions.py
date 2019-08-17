'''
Write a simple script that demonstrate your understanding of functions in python 
'''
num = int(input("Enter any number of your choice \n"))     #User inputs number

def factorial(num):                            #Function initialization
    if num == 0 or num == 1:
        return 1
    else:
        return num * (factorial(num - 1))

print('The factorial of %d is %d' % (num, factorial(num)))    #Function calling

sum = lambda arg1, arg2: arg1 + arg2     #Using lambda.
print("SUM=", sum(10,20))

def addition(num1,num2):
 total = num1 + num2
 print(total)
 return total

addition(10, 20)
 



