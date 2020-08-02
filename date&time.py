'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
#current time date and year

import datetime

curent_time = datetime.datetime.now()
print(curent_time)

# current week day/day

day = datetime.datetime.now()

print(day.strftime("%A"))

# current month

month = datetime.datetime.now()

print(month.strftime("%B"))


#current year

curent_year = datetime.datetime.now()

print(curent_year.year)

# current month-date-year

current = datetime.datetime.now()

print(current.strftime("%D"))
