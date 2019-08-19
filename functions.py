'''
Write a simple script that demonstrate your understanding of functions in python 
'''


#non-void funtion
def product(number1,number2):
    multiplication = number1 * number2
    print(multiplication)
    return


intNum = 8
intNum1 = 10

if((intNum < 10)and (intNum1 == 10)):
    product(intNum,intNum1)

#void function
def nothing():
    print('This is void')

nothing()