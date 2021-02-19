#lists
name=['Faith','Elizabeth','Paul','Evelyn','Inno']
print(name[0]) 
print(name[2:4]) 
print(name[2:]) 
name[4]='Innocent' 
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
        

