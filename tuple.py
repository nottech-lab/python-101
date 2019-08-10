'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''

#Python tuples are much like list except they are created using blackets instead of square brackets as list
#Another difference with a list is that tuples are immutable i.e. u cannot change data once in a tuple
#Example

developers = ("Tajr", 201, "Faith", 201.9, "Wikedz", 200)
print(developers)

developer_info = ('Python Programmer', ['python', 'Java', 'c++'], ('Web dev', 'AI expert', 'Frontend developer'))

for info in developer_info:
    print(info)


# Also Tuple elements can be accessed by using index just like a list
print()
for i in range(len(developer_info)):
    print(developer_info[i])  