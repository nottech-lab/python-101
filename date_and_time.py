# Date and Time
import time # time module.
print(time.time()) # returns number of seconds.
print(time.localtime()) # returns a tuple.
print(time.asctime()) # returns a string.
print(time.sleep(3)) # delays execution to 3 seconds.

import datetime
# creating a date
d = datetime.date(2019,9,15) 
print(d) # retuns a date

# today local time
tday = datetime.date.today() 
print(tday) # today local time.
print(tday.year) #  returns only year.
print(tday.day) # returns only day.
print(tday.month) # returns only month
print(tday.weekday) # returns day of the week, monday as 0, sunday as 6.
print(tday.isoweekday) # returns day of the week, monday as 1, sunday as 7.  

# creating timedelta.
tdelta=datetime.timedelta(days=7) # creating timedelta one week away.
print(tday+tdelta) # returns the day after one week.
print(tday-tdelta) # returns the day one week ago.

import calendar # calendar module.

print(calendar.month(2019,9)) # returns calendar of the month.
print(calendar.calendar(2019,3,1,10)) # returns calendar of the whole year.
print(calendar.isleap(2019)) # returns false since 2019 is not a leap year.