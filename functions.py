'''
Write a simple script that demonstrate your understanding of functions in python 
'''

#Functions
'''carries block of code'''

#Required functions
def addfun(x,y):
    return x + y
print(addfun(4, 8))  

#Keyword Functions
def data(name, gender):
    print("Name: ", name)
    print("Gender: ", gender)
    return
data(name = "Marcellus", gender = "Male")  

def number(var1, var2):
    sum = var1 + var2
    print("the answer is: ", sum)
    return sum
sum = number(50, 60)  


#Anonymous Functions
'''these functions use the lambda keyword'''
minus = lambda x, y: x - y
print(minus(8, 4))

#This function adds two numbers
def add(x, y):
    return x + y
#This function subtracts two numbers
def subtract(x, y):
    return x - y
#This function multiplies two numbers
def multiply(x, y):
    return x * y
#This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#put in a choice
choice = input("Enter choice: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if choice == 1:
    print(a + b, add(a, b))
elif choice == 2:
    print(a - b, subtract(a, b))
elif choice == 3:
    print(a * b, multiply(a, b)) 
elif choice == 4:
    print(a / b, divide(a, b))  
else:
    print("invalid input")                  



