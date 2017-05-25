#PROGRAM "".py
import Ex25UnitsOfTimeAgain

#SET conversion for day, hours, minutes and seconds
seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

#READ number of days, hours, minutes, seconds
days = int(raw_input("Enter total number of days:\n"))
hours = int(raw_input("Enter total number of hours:\n"))
minutes = int(raw_input("Enter total number of minutes:\n"))
seconds = int(raw_input("Enter total number of seconds:\n"))

#COMPUTE
d2ss = days * seconds_per_day
hh2ss = hours * seconds_per_hour
mm2ss = minutes * seconds_per_minute
total_time = d2ss + hh2ss + mm2ss + seconds

#WRITE number of days, hours, minutes, and seconds
print "%s D: %s HH: %s MM: and %s SS:" % (days, hours, minutes, seconds)
print "is a total of %s seconds.\n" % total_time

Ex25UnitsOfTimeAgain.seconds2_days(total_time)
#END
