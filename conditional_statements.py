''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''

def comparison(x, y):
    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')

def odd_even(x):
    if x % 2 == 0:
        print('x is even')
    else:
        print('x is odd')

x = int(input("Enter the value of integer x> "))
y = int(input("Enter the value of integer y> "))

comparison(x, y)
odd_even(x)

