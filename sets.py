'''
Write a simple script to demonstrate your understanding of sets as data types 
'''

number = set([1,2,3,4,5,6,7,8,9])
number1 = set([2,5,8,6,9])

# How to display all Number
for num in number:
    print(num)

number.add(10) #How to add item into number set

Union_Numbers = number|number1 # Union between Number and Number1 SET

intercNumber = number & number1 # Intersection between Number and Number1 SET
