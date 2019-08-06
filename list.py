list1 = ['abdc',123,'nottech',45]
print(list1)   #Print whole list
print(list1[0])  #Print first element of list
print(list1[2:4])  #Print list starting from 3rd to 4th

del list1[2]     #Delete second element in list
print(list1)

list1.remove('abdc')  #Remove abdc from list
print(list1)

list1.append('xyz') #Append value to the list
print(list1)

list2 = [8,6,9,10,22,4,1,3,2,5]
list2.sort()        #Sort the list
print(list2)