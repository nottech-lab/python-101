'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''
          # DICTIONARY.
          
# Is the collection which is ordered, changeable and indexed.

# Dictionaries are writen in curly  brackets.

# They have keys and values.

# Values can be extracted by the key name.

my_dict = {"Name": 'Daudi', "Date of birth": 19, "Year": 1997} # creating a dictionary.
print(my_dict) # print the dictionary

print(my_dict['Name']) # Access value of element by key.

my_dict['gpa'] = 3.7 # adding  key with its value in the dictionary.
print(my_dict)  # printing the dictionary.

my_dict.keys()  #get list keys of a dictionary.

my_dict.values()    # get list values in a dictionary.

for key , value in my_dict.items(): # get list key, values pairs item in a dictionary
    print("{0}: {1}".format(key, value))