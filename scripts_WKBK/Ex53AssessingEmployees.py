#PROGRAM 53.py3

#SET values for the types of raise
rating0 = "Unacceptable performance"
rating4 = "Acceptable performance"
rating6 = "Meritorous performance"
INVALID = "Invalid"

#READ rating from the user as float
rating = float(input("Enter the rating from [0.0, 0.4, 0.6 or greater]: "))

#COMPUTE match for key and value pairing of rating to meaning
#IF rating >= 0.6 THEN
if rating >= 0.6 :
    #SET rating6
    performance = rating6
#IF rating == 0.4 THEN
elif rating == 0.4 :
    #SET rating4
    performance = rating4
#IF rating == 0.0 THEN
elif rating == 0.0 :
    #SET rating4
    performance = rating0
#ELSE
else:
    #SET INVALID
    performance = INVALID
    rating = 0.0
#ENDIF

#COMPUTE performance to rating * 2400
employee_raise = rating * 2400

#WRITE raise amount 
print("That rating is considered %s." % performance)
print("It provides for a $%.2f raise amount" % employee_raise)

#END
