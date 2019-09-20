'''
Write a simple script that would take input from user using keyboard 
'''



name = input('Enter your name: ')

if (name == 'John'):
    print ('Hi!... Sir, welcome. Please confirm your age')

else:
     print ('Sorry!.. The owner was expected for someone called John')
    
age = input('Enter your age: ')

if (int(age) >= 18):
    print ('Now you can reserve your private spot for drinks')

else:
    print ('Sorry this area is for people from 18 years old and above')

print ('Have a goodnight pal')
    