'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''


animals = ('cow', 'goat', 'rabbit', 'ants', 'fish', 'lamb')
position = (1, 2, 3, 5, 8)

print(animals[0],' and ',animals[2], ' are in the same phylum')  #prints items present in index 0 and 2 in the tuple present in variable 'animals'

combination = animals + position     #creates new tuple

print(combination)

del(animals[0])

print(animals)   #this will produce an error since a tuple cannot be updated