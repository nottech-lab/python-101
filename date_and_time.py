'''
Write code exampled with comments that demonstrates your understanging of date and time.

'''
    # DATE AND TIME.

    import datetime

    dt = datetime.datetime.strptime("2019-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
    print(dt)
    from datetime import datetime, timedelta, timezone
    
    JST = timezone(timedelta(hours=+9))
    dt = datetime(2019, 1, 1, 12, 0, 0, tzinfo=JST)
    print(dt)
    # 2019-01-01 12:00:00+09:00
    print(dt.tzname())
    # UTC+09:00
    dt = datetime(2019, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
    print(dt.tzname)
    # 'JST'
    
    #  Subtracting months from a date accurately.
    
    import calendar
    
    from datetime import date
    
    def monthdelta(date, delta):
        m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
        if not m:
            m = 12
        d= min(date.day, calendar.monthrange(y, m)[1])
        return date.replace(day=d,month=m, year=y)
    next_month = monthdelta(date.today(), 1) #datetime.date(2016, 10, 23)
    
    # Date Formatting.
    # Time between two date-times
    
    from datetime import datetime
    a = datetime(2019,10,6,0,0,0)
    b = datetime(2019,10,1,23,59,59)
    a-b
    (a-b).days
    (a-b).total_seconds()
    
    # Parsing string to datetime object
    
    
    from datetime import datetime
    datetime_string = 'Aug 11 2019, 00:00:00'
    datetime_string_format = '%b %d %Y, %H:%M:%S'
    datetime.strptime(datetime_string, datetime_string_format)
    # datetime.datetime(2019, 10, 1, 0, 0)
    