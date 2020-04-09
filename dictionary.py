'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''
dict = {'eins':'one', 'zwei':'two', 'drei':'three', 'veir':'four', 'funf':'five'}
#Accessing values in dictionaries
print(dict['zwei'])

#Adding dictionaries
dict = {'eins':'one', 'zwei':'two', 'drei':'three', 'veir':'four', 'funf':'five'}
dict['zehn'] ='ten'
print(dict)

#Delete dictionary elements
dict = {'eins':'one', 'zwei':'two', 'drei':'three', 'veir':'four', 'funf':'five'}
del dict['veir'] #remove an enrty with the key
dict.clear() #remove all entries
del dict #deletes the dictionary

#Built in dictionary functions and methods
#using pop method
dict = {'eins':'one', 'zwei':'two', 'drei':'three', 'veir':'four', 'funf':'five'}
pop_ele = dict.pop('eins')
print("\n Dictionary after deletion: " + str(dict))
print("Value with popped key is: " + str(pop_ele))

#using get method
phone = input("Phone: ")
digit_mapping = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine',
    '0':'Zero'
}
output = " "
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)
