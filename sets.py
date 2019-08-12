'''
    Write a simple script to demonstrate your understanding of sets as data types 
'''
'''
    Sets come from mathematics, where they represent an unordered group of (usually) unique numbers. We can add a number to a set five 
    times, but it will show up in the set only once.

    There is no built-in syntax for an empty set as there is for lists and dictionaries; we 
create a set using the set()constructor.

we can use the curly braces of 
dictionary syntax to create a set, so long as the set contains values. If we use colons 
to separate pairs of values, it's a dictionary, as in {'key': 'value', 'key2':
'value2'}. If we just separate values with commas, it's a set, as in {'value',
'value2'}. Items can be added individually to the set using its addmethod.
'''

student_set = {'issa', 'mwailombola', 'mubve', 'michael', 'issa'}
print(student_set)
# As you might notice in the output the item issa appears twice in set declaration but when we print it to a screen only single entity have been shown

# add() function is used to add data in a set
student_set.add('djeko')
print(student_set)

# union operation
set_A = {'a','e','i','o','u'}
set_B = {'a','b','c','d','e','f','g'}

print(set_A.union(set_B)) # This print the union of a set in a single arbitary set

# intersection operation
print(set_A.intersection(set_B)) # This will print intersecting items between two sets

# Difference operation
print(set_A.symmetric_difference(set_B))
