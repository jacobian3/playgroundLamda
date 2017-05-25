# call from Ex24UnitsOfTime.py
def seconds2_days(seconds):
   #SET conversion for day, hours, minutes and seconds
    seconds_per_day = 86400
    seconds_per_hour = 3600
    seconds_per_minute = 60

    #READ  seconds 
    seconds = int(seconds)
    print "seconds from main: ", seconds

    #COMPUTE
    days = seconds / seconds_per_day
    seconds %= seconds_per_day
    hours = seconds / seconds_per_hour
    seconds %= seconds_per_hour
    minutes = seconds / seconds_per_minute
    seconds %= seconds_per_minute

    #WRITE number of days, hours, minutes, and seconds
    print "is(D:HH:MM:SS): %d:%02d:%02d:%02d:" % (days, hours, minutes, seconds)

seconds2_days(454028) #change before using??

