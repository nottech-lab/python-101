from pip._vendor.distlib.compat import raw_input


'''
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123
'''
n=int(raw_input())


def printFunction(n):
    array=[]

    i=0
    while i < n:
        array.append(i + 1)
        i=i + 1
    return array


array = printFunction(n)
for a in array:
    print(a,end='')