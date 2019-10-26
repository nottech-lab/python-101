'''
Write a simple script to demonstrate your understanding of dictionaries as data types
''' 

#keeping dictionary in order
from collections import OrderedDict

d = OrderedDict()
d['hello'] = 1
d['python'] = 2
d['learners'] =3
d['dictionary'] = 4

#THe outputs for "hello 1", "python 2", "learners 3", "dictionary 4"
for key in d:
    print(key, d[key])