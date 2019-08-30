'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''

kingdom = {'Kingdom': 'Animalia', 'Phylum': 'Mammalia', 'Genus': 'Homo', 'Species': 'Sapien'}

print(kingdom['Genus'])    #prints the value of the item with key 'Genus' in the 'kingdom' dictionary

kingdom['Common'] = 'Human Being'     #adds a new value in the dictionary with the key 'Common'

print(kingdom)

print(len(kingdom))   #prints the length of the dictionary

kingdom.clear()     #clears all the dictionary elements

print(kingdom)   #returns an empty dictionary