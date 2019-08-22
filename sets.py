'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
#A set is a collection which is unordered and unindexed.
vendor_set ={"Cisco","HPE/Aruba","Juniper","Huawei","Arista"}

#Access items
#You can't use index to access an item,the index change randomly
for items in vendor_set:
    print(items)

#Checking if an item exists in a set
print("Cisco" in vendor_set)

#Items can't be changed

#Adding an item
vendor_set.add("VMware")

#To add multiple,use update
vendor_set.update("RiverBed","Netscout")

#Removing an item
vendor_set.discard("Cisco")

#emptying the set
vendor_set.clear()

#deleting the set
del(vendor_set)