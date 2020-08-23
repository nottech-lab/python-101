'''
Write a simple script to demonstrate your understanding of lists 
'''
#lists
name=['Faith','Elizabeth','Paul','Evelyn','Inno']
print(name[0]) # indexes are used to acces item in list
print(name[2:4]) # The colon acceses names from index 2 inclusvely to index 4 exclusively
print(name[2:]) # The colon acces index 2 inclussively to the end
name[4]='Innocent' # changes the content at the given index
print(name)

#Creating 2d matrices
matrices=[
    [1,2,3],
    [4,5,6],
    [7,89]
]
print(matrices[0][1])
#iterating through a 2D array
for row in matrices:
    for number in row:
        print(number)
        

 # Methods found on a list
 days=[1,2,3,4,5]
 days.append(20) #adds more items at the end
 print(days)
days.insert(2,2) #insert number at the given index
 print(days)
 days.remove(5)
 print(days)
 days.pop() #removes the last item
 print(days)
  days.clear() #removes all items in a list
 print(days)
