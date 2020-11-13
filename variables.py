'''
Write a simple script to demonstrate your understanding of Variable,identifier and keywords
'''
#examples of values assigned to variables 
name =' universe '
point = ' a friendly'
print(point+ name)

#variables outside a function 

l = 'life'
def myfunc():
    l = 'God'
    print( l + 'is good')
myfunc()

print( l + 'is good')

# using the global keyword the variable inside the function becomes dominant

l = 'life'
def my_func():
    global l
    l = 'God '
    print( l + 'is good')
myfunc()

print( l + 'is good')

#an simple example of an identifier 

my_class1 = 'python 101'
print(my_class1)