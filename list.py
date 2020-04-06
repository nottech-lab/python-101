'''
Write a simple script to demonstrate your understanding of list 
'''
fruits = ['Apples', 'Bananas', 'Strawberries', 1994, 2015]
tiny_fruits = ['Raspberries', 'Blueberries']
#Accessing values on lists
print(tiny_fruits[1])

#Updating values in lists
fruits[0] = 'Mangoes'
#The value of index 0 will be replaced by mangoes

#Deleting list items
#from fruits the value of index 1 will be deleted from the list:
del fruits[1]

#Basic List Operators
#length
print(len(fruits))

#concatenation
print(fruits + tiny_fruits)

#repetation
print(tiny_fruits*2)

#membership
print(5 in fruits)

#iteration
for i in fruits:
    print(i)

#slicing and matrixes
print(fruits[1:])

#Built in list functions
#sort
fruits.sort()

#append(add an item in a list)-must be accompanied by an object
fruits.append('Guava')

#reverse(from right to left)
fruits.reverse()

'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''
#Instead of using a for loop
tiny_fruits = ['Raspberries', 'Blueberries']
new_fruits = []
for i in fruits:
    if filter(i):
        new_fruits.append(i)

#list comprehension can be used
new_fruits = [i for i in tiny_fruits if filter (i)]        