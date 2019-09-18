'''
Write a simple script to demonstrate your understanding of lists 
'''

names = ['John', 'Margret','Rachel','Innocent', 'Mohammed']
age = [10, 27, 45, 61, 30, 15]

print ('The oldest person has'), max(age), ('years old')
print ('The youngest person has'), min(age), ('years old')
print ('The longest name here is'), min(names)
print ('The shortest name here is'), max(names)
print ('The amount of names we have here is'), len(names)
print (names[1]), ('has'), (age[2]), ('years old')
print (names[0]), ('and'), (names[2]), ('are married couple. And their son'), (names[3]), ('has'), (age[0]), ('years old')