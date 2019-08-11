'''
Write a simple script that demonstrate your understanding of functions in python 
'''

   # FUNCTIONS.
# function is a useful device that groups together a set of statements so they can be run more than once.
# They can also let us specify parameters that can serve as inputs to the functions.
# functions allow us to not have to repeatedly write the same code again and again. 
# function in Python is defined by a def statement. The general syntax looks like this


def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (doc-string) goes
    '''
    # Do stuff here
    #return desired result
    
# definining and calling a simple function.

def greet_two(greeting="Howdy"):
    print(greeting)

greet_two()             # call the function without giving a value.


def many_types(x):
    if x < 0:
        return "Hello!" # Python functions can return values of any type via the return keyword.
    else:               # One function can return any number of diﬀerent types!
        return 0
print(many_types(1))    # output is 0
print(many_types(-1))   # output is Hello!


def do_nothing():       # no return, so the function will reach reach at the end of execution and retun None. 
    pass
print(do_nothing()) # Out: None


# defining a function with arbitary number of arguements.

def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)
func(1, 2, 3)  # Calling it with 3 arguments
# Out: 1
#      2
#      3
             
def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)
func(value1=1, value2=2, value3=3) # Calling it with 3 arguments
# Out:
#value1 1
#value2 2 
#value3 3
func() # Calling it without arguments
# No Out put

my_dict = {'foo': 1, 'bar': 2}

func(**my_dict) # Calling it with a dictionary.

# Lambda function(inline function).
# it has variable, arguement and expression.
# example.

greet_me = lambda: "Hello"
print(greet_me())

sq = lambda x: x**2
print(sq)


