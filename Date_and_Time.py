import time                     #Importing time module
import calendar                 #Importing calendar module

localtime = time.asctime(time.localtime(time.time()))
print("local time:", localtime)     #Print local area time

cal = calendar.month(2001,12)
print(cal)                    #Print callender of 2001 in december