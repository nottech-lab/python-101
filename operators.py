'''
Write a simple script that demonstrate your understanding of Operators,operands and operator precedence
'''
# Operators are particular sysmbols that are used to perform operation on operands and return the results that can be used in a program
# Operands refer to the items/values manipulated by an operators
# Example 7 + 8 = 15 here 7 and 8 are operands while + and = are operators and 15 is a result that can be used in a program
# Usually operands are either stored in variables or can be used as a literal like an example above
# Python supports the following operators
"""
    1). Arthimetic Operators
    2). Rational Operators
    3). Assignment Operators
    4). Logical Operators
    5). Membership Operators
    6). Identity Operators
    7). Bitwise Operators
"""

# Level of precedence in Python

""" 
    Below is a list of all Operators supported by python listed by considering the level of predicence

        ()      	        Parentheses
        **	                Exponent
        +x, -x, ~x	        Unary plus, Unary minus, Bitwise NOT
        *, /, //, %	        Multiplication, Division, Floor division, Modulus
        +, -	            Addition, Subtraction
        <<, >>	            Bitwise shift operators
        &	                Bitwise AND
        ^	                Bitwise XOR
        |	                Bitwise OR
        ==, !=, >, >=, <, <=, is, is not, in, not in	Comparisions, Identity, Membership operators
        not	                Logical NOT
        and	                Logical AND
        or	                Logical OR

    NOTE: For operators with the same level of precidence ASSOCIATIVITY helps to determine the order of operation 
          In python almost all the operators have left to right associativity             
"""
# EXAMPLES
print(4 * 3 // 7) # The output here is 1 since multiplicatin and floor division has the same level of precidence hence left-right associativity
print()

print(4 * (3 // 7))  # The output here is 0 since Parentheses has higher level of precidence and floor division retuns 0 ehich is multiplied by 4 to get 0 again
print()

# Exponent operators has right-left associativity as shown below
print(2 ** 3 ** 2) # The output here will be 512 since the operation is performed from right to left i.e. 3 power of 2 which is equal to 9 taken again as 2 power of 9 to get 512
print()

# Operators such as comparison and assignment operators they are considered non associative operators
print(20 < 3 < 5) # For this operators neither arrangement is equivalent even though in some cases you will have the same output
print()

print(5 < 3 < 20) # The output here is equivalent to the example above i.e False
print()

print(3 < 5 < 20) # The output here is True
print()

number1  = 5
number2  = number3 = number1
print("number1 = {}".format(number1))
print("number2 = {}".format(number2))
print("number3 = {}".format(number3))
print()
# #The following will result into an SyntaxError
# number2 = number3 -= number1
# print("number1 = {}".format(number1))
# print("number2 = {}".format(number2))
# print("number3 = {}".format(number3))

# MEMBERSHIP operators (in, not in) these are used to check if and operand belongs to a given set of values. See the example below
string = "Issa is typing now"
print("Issa" in string) # The output here is True since a substring Issa is a member of a given string above
print("Juma" in string) # The output here is False since a substring Juma is not a member of a given string above
print("Rajabu" not in string) # The output here is True since a substring Rajabu is not a member of a given string above
print()

# IDENTITY operators(is, is not) these are used to check if variables in either side points to the same object. See the example below
number = 20
if(type(number) is int):
    print("number example => This will evaluate to True ")
else:
    print("number example => This will evaluate to False")


age = 20
if(type(age) is not int):
    print("age example => This will evaluate to True ")
else:
    print("age example => This will evaluate to False")
