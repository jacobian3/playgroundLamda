## PROGRAM python3
# Convert a number of seconds to day, hours, minutes and seconds
#

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

#READ input from the user
seconds = int(input("Enter a number of seconds: "))

#COMPUTE the days, hours, minutes and seconds
days = seconds / seconds_per_day
seconds = seconds % seconds_per_day

hours = seconds / seconds_per_hour
seconds = seconds % seconds_per_hour

minutes = seconds / seconds_per_minute
seconds = seconds % seconds_per_minute

#WRITE results with desired formatting
print("The equivalent duration is", \
    "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))
