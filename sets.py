'''
Write a simple script to demonstrate your understanding of sets as data types 
'''

thisset = {"Mangos", "Oranges", "Bananas"}
for x in thisset:
    print (x)

print ('Mangos' in thisset)

print (len(thisset))

thisset.add('Pinapples')

for x in thisset:
    print(x)

thisset.update(['Apples', 'Tangerine'])

print (thisset)

print (len(thisset))

thisset.remove('Apples')
thisset.remove('Mangos')

print (thisset)

thatset = {'Maize', 'Wheat', 'Beans'}

bothsets = thisset.union(thatset)

print (bothsets)