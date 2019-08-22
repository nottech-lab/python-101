'''
Write a simple script to demonstrate your understanding of sets as data types 
'''

fruits = {'apple', 'orange', 'banana', 'grapes'}

#accessing sets
for fruit in fruits:
    print(fruit)

print("")
print("")
print('Is Rabbit in the set of animals? ','rabbit' in fruits)

#updating the set

fruits.add('guava')
print('Is Guava in the set of fruits? ','Guava' in fruits)

fruits.update(['Cucumber', 'Strawberry'])
for fruit in fruits:
    print(fruit)

#removing items
fruits.remove('Orange')
print('Is apple in the set of fruits? ','oranga' in fruits)