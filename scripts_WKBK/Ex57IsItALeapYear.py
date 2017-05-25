#PROGRAM Ex57.py3
def leap_year_validate(year):
    #year = int(input("Enter the year to check: "))

    if year % 400 == 0 :
        leap_year = True

    elif year % 100 != 0 and year % 4 == 0 :
        leap_year = True

    else: 
        leap_year = False

    return leap_year
   # print("Year: %s is %s" % (year, leap_year))
#END
