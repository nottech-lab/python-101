'''
Write a simple script to demonstrate your understanding of strings 
'''
#String can be represented using single or double quotes and triple quotes when its a paragraph
print('Elizabeth')
print("Elizabeth")
print('''My name is Elizabeth
I am an online student
I am happy to learn''')


# Some methods related to strings
name='Elizabeth'
print(len(name)) #obtains length of the string
print(name.upper()) # converts to uppercase
print(name.lower()) # converts to lowercase
print(name.find('l')) #returns the index of the first occurance of the letter
print(name.replace('Elizabeth','Mary')) #replaces one worrd with another or character with another
students='good morning sir'
print('gooD' in students) # checks if a word or a character is in a particular expression


#Character position
#indexing position begins from zero
name='Elizabeth'
print(name[2]) 
print(name[-1]) #outputs the first character from the end
print(name[2:-1]) #outputs a string begining from char of index 2 inclusive to char of index -1 exclusive
print(name[:1]) #considers the initial index 0 to 1
print(name[1:]) #considers char at index 1 to final
