#PROGRAM Ex03PrintAGrade :

# SET score to initial value to enter loop
score = 1 
# REPEAT request for score entry 
while True:
    # condition is is tested only after the first pass
    # initialization allows it to pass as True and then be
    # SET by the user
    if score < 0.0 or score > 1.0:
        print "Bad Score; Try again"
    #READ score between 0.0 and 1.0
    score = float(raw_input("Enter Score[0.0 to 1.0]:\n"))
    if not(score < 0.0 or score > 1.0): #UNTIL correct score is given
       break 
#IF score >= 0.9 THEN 
if score >= 0.9:
    #WRITE grade is an A
    print "grade is an A"
#IF score >=0.8 THEN
elif score >= 0.8:
    #WRITE grade is a B
    print "grade is a B"
#IF score >= 0.7 THEN
elif score >= 0.7:
    #WRITE grade is a C
    print "grade is a C"
#IF scroe >= 0.6 THEN
elif score >= 0.6:
    #WRITE grade is a D
    print "grade is a D"
#ELSE 
else:
    #WRITE grade is an F b/c score is < 0.6
    print "grade is a F"
#ENDIF
#END
