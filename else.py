'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format
'''#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #n = int(input())
#n = int("input(Enter the number: "))
if (n%2)==1:
    print("Weird")
elif(n in range (2,5) and (n%2)==0):
    print("Not Weird")
elif(n in range (6,20) and (n%2)==0):
    print ("Weird")
elif(n<=100 and (n%2)==0):
    print("Not Weird")
else:
    print("Out of range")           
