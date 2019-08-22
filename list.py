'''
Write a simple script to demonstrate your understanding of lists 
'''
#List is a collection which is ordered and changeable. Allows duplicate members.
vendor_lists =["Cisco","HPE/Aruba","Juniper","Huawei","Arista"]

#Accessing items
print(vendor_lists[1])

#change item value
vendor_lists[3]="VMware"

#looping in the list
for vendors in vendor_lists:
    print(vendors)

#checking if an item is present
if "Dell"in vendor_lists:
    print("Yes Dell is in vendor list")
else:
    print("Not available")

#checkig the length of the list
print(len(vendor_lists))

#adding item
vendor_lists.append("Riverbed")

#removing an item
vendor_lists.remove("VMware")

#remove a specified index or last item
vendor_lists.pop()
vendor_lists.pop(3)

#emptying the list
vendor_lists.clear()

#copying the list 
Worldwide_vendors = vendor_lists.copy()

#creating a list using keyword List
New_vendors =list(("Cisco","HPE/Aruba","Juniper","Huawei","Arista","Netscout"))


