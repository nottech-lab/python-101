'''
Write a simple script to demonstrate your understanding of lists
'''

def remove_duplicates(list_1, list_2):
    list_1_copy = list_1[:]

    for i in list_1_copy:
        if i in list_2:
            list_1.remove(i)

    return list_1

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 5, 6]

print(remove_duplicates(list_1, list_2))
