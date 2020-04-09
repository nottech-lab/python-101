'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''
#tuples
'''immutable data structure, that is: they can not be changed'''
#Accessing values in dictionary
t = ('Subaru', 'Toyota', 'Nissan', 'Audi', 'Lamborghini')
print(t[3])
print(t[1:4])

#Deleting tuple
t = ('Subaru', 'Toyota', 'Nissan', 'Audi', 'Lamborghini')
del t #deleting the tuple


#Basic Tuple Operators
#1.length
print(len(t))

#2.concatenation
t = ('Subaru', 'Toyota', 'Nissan', 'Audi', 'Lamborghini')
tup = ('Ferrari', 'Bugatti')
print(t + tup)

#3.iteration
t = ('Subaru', 'Toyota', 'Nissan', 'Audi', 'Lamborghini')
for i in range(t):
    print(i)

#convert tuple to list
tuple = [(1, 2), (3, 4), (5,6)]
result = []
for i in range(tuple):
    for x in i:
        result.append()
print(result)        

