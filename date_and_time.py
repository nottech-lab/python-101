'''
Write code exampled with comments that demonstrates your understanging of date and time.

'''
    # DATE AND TIME.

    import time # time module
    
    print(time.time()) # returns current time stamp i.e numbers of seconds between january up to current time second.

    print(time.localtime()) # gives the tuple representation of number of seconds returned by time function.

    print(time.asctime()) # gives the string representation of tuple returned by localtime function.

    time.sleep(6) # delays execution to 6 seconds.
    print("Python") # it can gives the word 'Python' after 6 seconds.
    
    import datetime
    from datetime import date, timedelta

    # creating a date
    d = datetime.date(2019,8,29)
    print(d)

    # today local time
    tday = datetime.date.today()
    print(tday)
    
    print(tday.year) # it gives only a year.
    
    print(tday.day) # it gives only a day.

    print(tday.month) # it gives only a month.
    
    print(tday.weekday) # it gives the day of the week starting monday as 0 and sunday as 6.

    print(tday.isoweekday) # it gives day of the week starting monday as 1 and sunday as 7.
    
    tdelta = datetime.timedelta(day=7) # creating a timedelta one week away.
    print(tday+ tdelta) # gives the day after on week from current day.

    print(tday-tdelta) # gives the day one week ago.

    import calendar # import the calendar modele.
    
    print(calendar.month(2019, 8)) # gives the calendar of August.
    # month function takes 2 arquements to specify year and month.

    print(calendar.calender(2019, 3, 1, 10)) # calendar of the whole year
    # calendar function takes four arguements, year to specify year, maximum width a date occupy, length as the step between each week, and space between each column. 

    print(calender.isleap(2019)) # returns false since 2019 is not a leap year.

    