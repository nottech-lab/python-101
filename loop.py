'''
Write a simple script that demonstrate your understanding of loops in python   
'''
#for loop with declared variables
records = [
    ('hello, 1 , 2'),
    ('python', 'geeks'),
    ('hello, 3, 4'),
]

def do_hello(x, y):
    print('hello', x, y)
    
def do_python(s):
    print("python", s)
    
for tag, args in records:
    if tag == 'hello':
        do_hello(*args)
    elif tag == 'hello':
        do_hello(*args)