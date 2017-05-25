#PROGRAM Ex49.py3

#READ magnitude from user as float
magnitude = float(input("Enter the magnitude of the earthquake:\n"))

#COMPUTE selection based on range of input
#This logic is similar to grading program: Highest at the top and fall through
#is at the ending else statemtnt

#IF magnitude is >= 10 THEN
if magnitude >= 10 :
    #SET descriptor to Meteoric
    descriptor = "Meteoric"
#IF magnitude is >= 8 THEN
elif magnitude >= 8 :
    #SET descriptor to Great
    descriptor = "Great"
#IF magnitude is >= 7 THEN
elif magnitude >= 7 :
    #SET descriptor to Major
    descriptor = "Major"
#IF magnitude >= 6 THEN
elif magnitude >= 6 :
    #SET descriptor to Strong
    descriptor = "Strong"
#IF magnitude >= 5 THEN
elif magnitude >= 5 :
    #SET descriptor to Moderate
    descriptor = "Moderate"
#IF magnitude >= 4 THEN
elif magnitude >= 4 :
    #SET descriptor to Light
    descriptor = "Light"
#IF magnitude >= 3 THEN
elif magnitude >= 3 :
    #SET descriptor to Minor
    descriptor = "Minor"
#IF magnitude >= 2 THEN
elif magnitude >= 2 :
    #SET descriptor to Very minor
    descriptor = "Very minor"
#ELSE
else:
    #SET descriptor to Micro
    descriptor = "Micro"

#WRITE discriptor message to user
print("A %s magnitude is considered to be %s" % (magnitude, descriptor))
#END
