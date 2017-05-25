#PROGRAM Ex38MonthNameToNumberOfDays.py3

#READ  month from a user
month = input('Enter name of the month: ')

#SET assume that days are 31 as init condition, then test for variation
days = 31

#IF month is from set with 30 days THEN
if month == 'November' or month == 'September' or \
    month == 'June' or month == 'April':
    #SET days to 30
    days = 30

##IF month is Feburary and is set with 28 or 29  days THEN
elif month == 'Feburary':
    #SET days to 30
    days = "28 or 29"

#WRITE number of days of the month from the user
print("%s has %s days" % (month, days))
#END-IF
#END
