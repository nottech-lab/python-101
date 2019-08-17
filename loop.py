'''
Write a simple script that demonstrate your understanding of loops in python   
'''

#while loop
number = 1

while(number <= 5):
    print("The number is : ",number)
    if(number==4):
        break
    number += 1


print("The End!")
print("")
print("")

#for loop
numbers = [1, 2, 5,6]

for number in numbers:
    print("The number is: ", number)
