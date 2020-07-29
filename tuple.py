'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''
employee = ("Josephine","Monica","Erasto","Mugube")
print(employee)
print(employee[1])
print(employee[:1])
print(employee[2:3])
print(employee[-4])
print(employee[:4])
print(employee[4:])


#convert the tuple into a list to be able to change it
x = ("mango","banana","pasion")
y = list(x)
y[1] = "cherry"
x = tuple(y)

print(x)

#loop trough a tuple
employee = ("vodacom","safaricom","tigo")
for x in employee:
    print(x)

#if statement in tuple
employee = ("vodacom","safaricom","tigo")    
if "tigo" in employee:
    print("Yes,'tigo' is in the employees tuple")
    
#Tuple length    
employee = ("tigo","vodacom","safaricom")
print(employee)
print(len(employee))

#additem
employee = ("tigo","vodacom","safaricom")
employee2 add (hello[2])
print(employee)
