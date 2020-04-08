Task 1
Print Hello, World!

code print("Hello, World!")

Task 2:If-Else 

Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

Code:

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

TASK 3

Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, . The second line contains the second integer, .

Output Format

Print the three lines as explained above.

CODE
if __name__ == '__main__':
    if __name__ == '__main__':
        firstno=int(input("Enter first Number").strip())
        secondno=int(input("Enter second Number").strip())
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)

add(firstno, secondno)
sub(firstno,secondno)
mult(firstno,secondno)

TASK 4
Task
Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, . The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333

CODE
if __name__ == '__main__':
    if __name__ == '__main__':
        firstno=int(input("Enter first Number").strip())
        secondno=int(input("Enter second Number").strip())
def divint(a,b):
    num = int(a/b)
    print(num)
def divfloat(a,b):
    num2 = float(a/b)
    print(num2)


divint(firstno, secondno)
divfloat(firstno,secondno)