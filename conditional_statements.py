''' 
    Write a simple script that demonstrate your understanding of conditional statements 
    Simple If , if else , elif  
'''

# CONSIDER A GIVEN TASK BELOW
"""
    Given an integer, n , perform the following conditional actions:
        If n is odd, print Weird
        If n is even and in the inclusive range of 2 to 5, print Not Weird
        If n is even and in the inclusive range of 6 to 20, print Weird
        If n is even and greater than 20, print Not Weird

    Input Format
        A single line containing a positive integer, n.

    Constraints
        1 <= n <= 100 

    Output Format
        Print Weird if the number is weird; otherwise, print Not Weird.

    Sample Input 0
        3

    Sample Output 0
        Weird

    Explanation 0
        n = 3
        n is odd and odd numbers are weird, so we print Weird.

    Sample Input 1
        24

    Sample Output 1
        Not Weird

    Explanation 1
        n = 24
        n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.
""" 
# Variable declaration and Input Gathering
number = eval(input("Please enter an integer: "))

# Setting out a range of inputs to be 1 <= n <= 100  
if number in range(1, 101):
    # Cheking if entered integer is an even number or odd number
    if number % 2 == 0:
        # Implementation of even number logics
        if number in range(2,6):
            print("Not Weird")
        elif number in range(6,21):
            print("Weird")
        elif number > 20:
            print("Not Weird")
    else:
        print("Weird")
else:
    print("{} is not within a range of 1 - 100. Please enter an integer within a range".format(number))        
