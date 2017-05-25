#PROGRAM Ex58.py3
import Ex57IsItALeapYear

#READ 
current_date = input("Enter date in format: [YYYY-MM-DD(no leading zeros)]: ")
#???? how to correct 01 in mm and dd???
#will cause syntax error

yyyy = int(current_date[:4])
mm = int(current_date[5:7])
dd = int(current_date[-2:])


#COMPUTE from month the maximum number of days
#SET assume that days are 31 as init condition, then test for variation
days_max = 31

#COMPUTE how many days_max are there in the selected mm; see Ex38
#IF mm is 30 day month THEN
if mm == 11 or mm == 9 or \
    mm == 5 or mm == 4 :
    #SET days_max to 30
    days_max = 30

#IF mm is february THEN
elif mm == 2 :
    #CALL leap year validation with year; Ex58.py3
    leap_year = Ex57IsItALeapYear.leap_year_validate(yyyy)

    #IF leap year THEN
    if leap_year == True :
        #SET number of days_max to 28
        days_max = 28
    #ELSE
    else:
        #SET number of days_max to 29
        days_max = 29
    #ENDIF

#COMPUTE day,month, and year increment
#Assume next year is current year, until changed 
#Assume next month is current month, until changed
next_year = yyyy
next_month = mm

#IF mm != 12 THEN
if mm != 12 :
    #IF day is day max in month THEN
    if dd == days_max :
        #SET mm += 1
        next_month = mm + 1
        #SET next day is 1
        next_day = 1
    #ELSE
    else:
        #SET next day is dd + 1
        next_day = dd + 1
    #ENDIF
#ELSE
else:
    #IF day is day max in month and month is 12 THEN
    if dd == days_max :
        next_year = yyyy + 1
        next_month = 1
        next_day = 1
    #ELSE
    else:
        #SET next day is dd + 1
        next_day = dd + 1
    #ENDIF
#ENDIF

#WRITE the next date as one statement
#???next_date = ?how to do as one statement??

#print("For day: %s, the next day is: %s" % (current_date, next_date) )
print("For day: %s" % current_date)
print("Next Year: %s" % next_year)
print("Next Month: %s" % next_month)
print("Next day: %s" % next_day)
#END

