'''
Write a simple script that demonstrate your understanding of functions in python 
'''

#A block of code which runs after its called
#Creating a function
def myname():
    print("My name is Joseph Karage")

#Calling a function
myname()

#Using parameters
def scores(man_u,wolves):
    print(f"The match ended manchester united{man_u} wolvehampton{wolves}")
scores(1,1)

#Passing list as parameter
def players(man_u):
    for i in man_u:
        print(i)

man_u=["De gea","Martial","Rashford","Pogba"]
players(man_u)

#Using the return statement
def square(number):
    return number*number
print(square(5))


#Arbitrary arguments,when number of arguments are unknown
def my_nicknames(*nicknames):
    print("my best nickname is:"nicknames[3])

my_nicknames("janjosy","jk3","hosee","jk",)


#Recursion function example
#gives 24
def factorial(n):    
    if n == 1:
        print(n)
        return 1    
    else:
        print (n,'*', end=' ')
        return n * factorial(n-1)

factorial(4)



