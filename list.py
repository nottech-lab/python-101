'''
Write a simple script to demonstrate your understanding of lists 
'''

animals = ['cow', 'goat', 'rabbit', 'ants', 'fish', 'lamb']
position = [1, 2, 3, 5, 8]

print("The length is of variable 'animals' is ", len(animals))     #'len' shows the length of items present in the list

animals[4] = 'pig'  #replaces item in index 4 (fish) to "pig" in the list present in variable 'animals'

print(animals)

print(animals[0],' and ',animals[5], ' are in the same phylum')  #prints items present in index 0 and 5 in the list present in variable 'animals'

del(animals[4])   #removes item in index 4

print(animals)

number = 0
number1 = 0

while(number<len(animals)):
    while(number1<len(position)):
        print(animals[number], ' is in position ',position[number1])
        number1 += 1
        number += 1
