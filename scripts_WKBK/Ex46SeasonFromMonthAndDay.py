#PROGRAM Ex46.py3

#READ the month and day from the user
month = input("Enter the month[January, February, etc.]:\n")
day = int(input("Enter the day:\n"))

#IF 
if month == 'January' or month == 'February':
    season = 'Winter' 
#IF month is March THEN       
elif month == 'March' :
    #IF day is < 20 THEN
    if day < 20 :
        #WRITE winter
        season = 'Winter'
    #ELSE
    else:
        #WRITE spring
        season = 'Spring'
    #END-IF

#IF month is April or May THEN
elif month == 'April' or month == 'May' :
    #WRITE spring
    season = 'Spring'
#IF month is June THEN
elif month == 'June' :
    #IF day < 21 THEN
    if day < 21 :
        #WRITE spring
        season = 'Spring'
    #ELSE
    else:
        #WRITE Summer
        season = 'Summer'
    #END-IF

#IF month is August or July THEN
elif month == 'August' or month == 'July' :
    #WRITE  summer
    season = 'Summer'
#IF month is September THEN
elif month == 'September' :
    #IF day is less than 22 THEN
    if day < 22 :
        #WRITE summer
        season = 'Summer'
    #ELSE
    else:
        #WRITE Fall
        season = 'Fall'

#IF month is October or November THEN
elif month == 'October' or month == 'November' :
    #WRITE Fall
    season = 'Fall'
#IF month is December THEN
elif month == 'December' :
    #IF day is less than 21 THEN
    if day < 21 :
        #WRITE Fall
        season = 'Fall'
    #ELSE
    else:
        #Write Winter
        season = 'Winter'
    #END-IF
#END-IF #?? why is ending with else causing an error
print("The season is %s" % season)
#END
