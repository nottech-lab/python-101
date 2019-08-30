'''
Write a simple script to demonstrate your understanding of sets as data types 
'''


animals = {'cow', 'goat', 'rabbit', 'ants', 'fish', 'lamb'}

#accessing sets
for animal in animals:
    print(animal)

print("")
print("")
print('Is Rabbit in the set of animals? ','rabbit' in animals)

#updating the set

animals.add('Shark')
print('Is Shark in the set of animals? ','Shark' in animals)

print("")
print("")

animals.update(['Rhino', 'Lion'])
for animal in animals:
    print(animal)

#removing items

animals.remove('ants')
print('Is ants in the set of animals? ','ants' in animals)