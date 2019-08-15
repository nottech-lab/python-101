''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''
x = 10
if x > 0 and x <= 10:
    print('X is greater than 0 and equal to 10')
    
if x == 10:                      
    print('Found the value of x')
else:
    print('The value of x is not found')    

x  = 10
list_ = [1, 2, 3, 5]
if x in list_:
    print('x is found in list')
elif x not in list_:
    print('x is not found in list')
else:
    print('Choose again')    
