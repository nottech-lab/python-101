'''
	Task 2:If-Else 

	Given an integer,n , perform the following conditional actions:

	If  is odd, print Weird
	If  is even and in the inclusive range of 2 to 5, print Not Weird
	If  is even and in the inclusive range of  6 to 20, print Weird
	If  is even and greater than 20, print Not Weird
	Input Format

	A single line containing a positive integer, .

	Constraints

	Output Format

	Print Weird if the number is weird; otherwise, print Not Weird.

	Sample Input 0


'''

# Code
n = int(input("Enter integer number "))
flag = n % 2
if(flag == 1):
    print("Weird")
elif((flag == 0) and (n >= 2) and (n <= 5)):
    print("Not Weird")
elif((flag == 0) and (n >= 6) and (n <= 20)):
    print("Weird")
elif((flag == 0) and (n > 20)):
    print("Not Weird")
else:
    print('Wrong number')
