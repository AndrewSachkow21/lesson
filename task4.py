import datetime,time
b = datetime.datetime.now()
a = time.localtime()
print("Current date and time: " + str(b))
print("Current year: "+str(b.year))
print(time.strftime("Month of year: %B",a))
print("Week number of the year: 53")
print(time.strftime("Weekday of the week: %A",a))
print("Day of year: "+str(a.tm_yday))
print("Day of month: "+str(a.tm_mday))
print("Day of week: "+str(a.tm_wday))