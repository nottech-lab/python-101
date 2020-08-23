'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''
# Stores attributes of a thing(characteristics of a thing


Elizabeth={
    'age':10,
    'school':'Mazinde Juu',
    'is old enought':'True'
}
# Accesed by square bracket method
print(Elizabeth['school'])
print(Elizabeth.get('age')) # with get method if you enter the wrong key it wont lead to error
# adding to the dictionary
Elizabeth['Birthdate']='1/11/2020'
print(Elizabeth['Birthdate'])
