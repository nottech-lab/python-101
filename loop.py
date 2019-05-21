'''
Write a simple script that demonstrate your understanding of loops in python   
'''
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!\n\n')




def print_letters(name):
    for letter in name:
        print(letter)


countdown(10)
name = "Enock"
print_letters(name)
