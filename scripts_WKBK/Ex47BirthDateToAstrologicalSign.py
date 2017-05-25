#PROGRARM Ex47.py3
month = input("Enter the month[January, February, etc.]:\n")
day = int(input("Enter the day:\n"))

if month == 'January' :
    if day <= 19 :
        sign = "Capricorn"
    else:
        sign = "Aquarius"
elif month == 'February' :
    if day <= 19 :
        sign = "Aquarius"
    else:
        sign = "Pisces"
elif month == 'March' :
    if day <= 20 :
        sign = "Pisces"
    else:
        sign = "Aries"
elif month == 'April' :
    if day <= 19 :
       sign = "Aries"
    else:
       sign = "Taurus"
elif month == 'May' :
    if day <= 20 :
       sign = "Taurus"
    else:
       sign = "Gemini"
elif month == 'June' :
    if day <= 20 :
       sign = "Gemini"
    else:
       sign = "Cancer"
elif month == 'July' :
    if day <= 22 :
       sign = "Cancer"
    else:
       sign = "Leo"
elif month == 'August' :
    if day <= 22 :
       sign = "Leo"
    else:
       sign = "Virgo"
elif month == 'September' :
    if day <= 22 :
       sign = "Virgo"
    else:
       sign = "Libra"
elif month == 'October' :
    if day <= 22 :
       sign = "Libra"
    else:
       sign = "Scorpio"
elif month == 'November':
    if day <= 21 :
       sign = "Scorpio"
    else:
       sign = "Sagitarious"
elif month == 'December' :
    if day <= 21 :
       sign = "Sagitarious"
    else:
       sign = "Capricorn"

print("The zodiac sign is %s" % sign)
