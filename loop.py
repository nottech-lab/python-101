'''
Write a simple script that demonstrate your understanding of loops in python   
'''

    # LOOPS.
    
# While statements.

# The while statement allows you to repeatedly execute a block of statements as long as a condition is true.

# while some_condition:
#     algorithm

# Example

i = 1
while i < 5:
    print("The square root of {0} is {1}".format(i, i**2))
    i = i+1

    # FOR LOOPS

# A for loop acts as an iterator in Python.

# for variable in something:
#       algorithm

for i in range(6): # outputs integers of the specified range.
    print(i)

    # NESTED LOOP.
    
# Example.
for g in range(1, 6):
    for k in range(1, 3):
        print('%d %d = %d' % (g, k, g*k))

   # LOOP CONTROL STATEMENTS.
# loop control statements are break, continue and pass statements.

# break statement.
# used for terminates any types of loop.
count = 0
while count <= 100:
    print(count)
    count += 1
    if count >= 3:
        break
# continue statement.
# work somewhat like a break statement instead of forcing termination.
# it forces the next iteration of the loop to take pace, skiping any code in between.

for x in range(10):
# check whether x is even
    if x % 2 == 0:
        continue
    print(x)
# pass statement.
# used when a statement is required syntactically.
# you do not need any command or code to execute.
for letter in 'jobseeder':
    if letter == 's':
        pass
        print('pass block')
    print('current letter is:', letter)
