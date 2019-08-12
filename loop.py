'''
Write a simple script that demonstrate your understanding of loops in python   
'''
# loops are used to define the iteration inside a program
# They allow a specific block of a statements to be executed multiple times
# They are much more used when we have a collection like a list or tuple
# Python supports for loops as well as ehile loops see example below

item_list = ['issa',1,2,4,4.5,"John", ('manga', 'halima', 'salma',200, 20.5, 'John', 980, True),{'Location': 'Dar es salaam', 'Lab': 'Nottech Lab'}]

# to access the elements in item_list list all at once we need to define a machanism to loop througth
# for loop is suitable for the job up ahead

for item in item_list:
    print(item)
print()

# A you can see the item_list list caontain some other data structures like tuple and dictionary which are also iterable 
i = 0
while i < len(item_list[6]):
    if type(item_list[6][i]) == str:
        print(item_list[6][i])
    else:
        pass    
    i += 1