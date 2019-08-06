tuple1 = ('abdc',123,'nottech',45)
print(tuple1)   #Print whole list
print(tuple1[0])  #Print first element of list
print(tuple1[2:4])  #Print list starting from 3rd to 4th

print(len(tuple1))  #Print length of the tuple1

tuple2 = (12, 23, 45)
print(max(tuple2))  #Print maximum value in tuple2

x = 23
if x in tuple2:
    print('X is in tuple2')
else:
    print('X is not in tuple2')     
