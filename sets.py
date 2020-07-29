'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
#Python date
import datetime

x = datetime.datetime.now()
print(x)

####Year and Day
import datetime
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#create day object
import datetime
x = datetime.datetime(2020 ,8, 26)
print(x)

#Display the name of month
import datetime
x = datetime.datetime(2010 , 2 ,3)
print(x.strftime("%B"))

import datetime
x = datetime.datetime("2000")
print(x)
print(shrftime("%A"))




