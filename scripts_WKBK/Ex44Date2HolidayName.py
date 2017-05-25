#PROGRAM Ex44.py3
holiday_name = "no fixed-day holiday"

#READ the month and day from the user
month = int(input("Enter the month:\n"))
day = int(input("Enter the day:\n"))

#IF month and day match holiday listed THEN
if month == 1 and day == 1 :
    #WRITE holiday name
    holiday_name = "New year's Day"
elif month == 6 and day == 1 :
    #WRITE holiday name
    holiday_name = "Canada day"

elif month == 12 and day == 25 :
    #WRITE holiday name
    holiday_name = "Christmas day"

#ELSE
else:
    pass

print("month %s and day %s correspond to %s" % (month, day, holiday_name))
#end
