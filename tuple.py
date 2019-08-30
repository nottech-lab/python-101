'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''
#A tuple is a collection which is ordered and unchangeable
vendor_tuple =("Cisco","HPE/Aruba","Juniper","Huawei","Arista")

#Accesing items
print(vendor_tuple[1])

#Looping through a tuple
for items in vendor_tuple:
    print(items)

#Checking if an item exists
if "Huawei" in vendor_tuple:
    print("Huawei is among networking vendors")

#checking tuple length
print(len(vendor_tuple))