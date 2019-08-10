'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''

print("\t\tDICTIONARY")
print()
#Python Dictionaries are an unordered set of key and value
#Declared using curly brackets in python
#Example
developer = {'Name': 'Tajr', 'Occupation': 'Developer', 'Experience Rate': 201}
print(developer)
print()

# Acccessing Dictionary values via keys
print(developer['Name'])
print(developer['Occupation'])
print(developer['Experience Rate'])
print()

# Iteration in dictionary is defined by a keys() function which return list of keys to access
keys = developer.keys()
for key in keys:
    print(developer[key])

print()   
# KeyError Occur when we try to access the key in dictionary which doesnot exist
# print(developer[6])

# Updating Disctionary elements
# Multiple ways are available when it comes to update the dictionary. See the examples below

developer["Language"] = "Python" # This will add key language and value python to a developer dictionary
print(developer)
print()

developer['Name'] = "Issa Juma" # This will update the existing name value from Tajr to Issa Juma
print(developer)
print()

# del satatement can be used to delete elements in a dictionary
del developer["Experience Rate"] # This will delete the exerience rate key value pair
print(developer)
print()

# To delete the entire dictionary use del statement without square brackets
students = {"Primary" : "Issa Juma", "Secondary" : "Djeko Oct", "Diploma" : "Jeffer Will"}
print(students)
print()

del students
# print(students) This will result in a NameError since the students dictionary have been deleted
   