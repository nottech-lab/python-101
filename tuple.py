'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''

tup1 = ('John', 'Margreth', 'Rachel', 'Innocent', 'Mohamed')
tup2 = (10, 45, 60, 15, 32)


print ('The longest name is '), min(tup1)
print ('The shortest name is '), max(tup1)
print ('The oldest person has '), max(tup2), ('years old')
print ('The youngest person has '), min(tup2), ('years old')
print ('The first list has '), len(tup1), ('people')
print (tup1[1]*5)

tup3 = tup1[0:2] + tup2[2:4]
print (tup3)

del tup3

print (tup3)