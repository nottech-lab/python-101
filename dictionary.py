'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''

dict = {'name': 'Tana', 'age': 26, 'class': 'First'}



print (dict)
print str(dict)

print ('The length of dictionioray is'), len(dict)
print ('Type of data is '), type(dict)

dict['age'] = 30
dict['region'] = 'Dar es salaam'

print (dict)
print (dict['name']), (dict['age']), (dict['region'])