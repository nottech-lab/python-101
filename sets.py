'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
# creating a set of numbers.
num_set={1,3,2,4} 
print(num_set)
# add  one item into a set.
num_set.add(9) 
print(num_set)
# adding multiple element.
num_set.update([6,7,8]) 
print(num_set)
# remove one element.
num_set.discard(1) 
print(num_set)
# removev all elements.
num_set.clear()
print(num_set)
# remove one element.
num_set.remove(3) 
print(num_set)
# remove the last item.
num_set.pop()
print(num_set)
# delete the set.
del num_set 
print(num_set) # raise an error. 
