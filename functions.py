'''
Write a simple script that demonstrate your understanding of functions in python 
'''
# function preventing rewriting of code and enables code to be reused
# Example of function without return statement
def greet_user(your_name):
    print(f'Hellow {your_name},Good morning')
    print('How can i help you today')


the_name=input('What is your name')
greet_user(the_name)

# function with return statement
def addition(number1,number2):
    sum_of_numbers= number1 + number2
    return sum_of_numbers


the_sum=addition(2,5)
print(the_sum)

