'''
Write a simple script that demonstrate your understanding of loops in python   
'''
#Printing NOTTECH LAB to infinite Loop
while(True):
    print("NOTTECH LAB")

#Printing A WORD into Iteration Entered by USER
num = int(input("Enter Iteration: "))
word = input("Enter Word To Print: ")
nottech = 0
while(num > nottech):
    print(word)
    nottech +=1
else:
    print(word + " PRINTED: " + str(num) + " Times")

