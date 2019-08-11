'''
Write a simple script to demonstrate your understanding of lists 
'''
        # LISTS.
        
#name, gender, height, age, region, status
        
data = ["Daudi Mwanja", "M", "179", 28, "Dodoma", 1]

print(data) # print the list.

print(data[0])  # access the first value in a list.

print(data[0:2]) # first two values in a list.

print(data[-1])  # access the last value in a list.

data.append("350K") # add a value to the end of the list.
print(data) # print the list.

for item in data: # access all elements in a lis
    print(item) # print the list.
    
data.insert(1, "weight") # inserting a value at position index 1
print(data) # print the list.

data.remove(1) # remove the first item in the list.
print(data)   # Print the list.

data.clear() # Remove all items in the list.
print(data) # print the list.

