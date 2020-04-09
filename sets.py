'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
#Updating a set
my_set = set('a', 'c')
my_set.add('g')  #add a single value
my_set.update(['d', 'f'])
my_set.update(['b', 'e'], {'h', 'i'})
print(my_set)

#Remove elements
my_set = set('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
my_set.discard('h') #discard an element
my_set.remove('f')  #removes an element
print(my_set)

#Set Operations
#1.set union
sa = set(1, 2, 3, 4, 5)
sb = set(4, 5, 6, 7, 8)
print(sa | sb)

#2.set interception
sa = set(1, 2, 3, 4, 5)
sb = set(4, 5, 6, 7, 8)
print(sa & sb)

#3.set difference
sa = set(1, 2, 3, 4, 5)
sb = set(4, 5, 6, 7, 8)
print(sa - sb)

#symmetric difference
sa = set(1, 2, 3, 4, 5)
sb = set(4, 5, 6, 7, 8)
print(sa ^ sb)
