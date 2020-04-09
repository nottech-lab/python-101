'''
Write a simple script that demonstrate your understanding of loops in python   
'''

'''Python  for loops
Used to iterate over a sequence'''
names = ['Davina', 'Fergus', 'Exodus']
for i in names:
    print(i)

#The Break statement:
'''stops the loop before it has looped through all the items
there are cases here'''
#1.case 1
names = ['Davina', 'Fergus', 'Exodus']
for i in names:
    print(i)
    if i == "Fergus":
        break
#this gives Davina and Fergus

#2.case 2
names = ['Davina', 'Fergus', 'Exodus']
for i in names:
    if i == "Fergus":
        break
    print(i)
#this gives Davina only    

#The Continue statement
'''we can stop the current iteration of the loop, and continue with the next'''
names = ['Davina', 'Fergus', 'Exodus']
for i in names:
    if i == 'Fergus':
        continue
    print(i)

#The range(x) function
for i in range(1, 9):
    print(i)   


#The Python While Loop
'''repeats the condition till required'''
i = 1
while i < 6:
    print(i)
    i += 1 

#The break statement
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

#The Continue statement
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue 
    print(i)

#The else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is greater than 6")
