#PROGRAM Ex04.7GradeProgram.py

#READ value from user
grade = float(raw_input("Enter a score[0 - 1]:"))
    
#COMPUTE grade
#IF grade is > .9 THEN
if grade >= .9 :
    #WRITE A
    print("grade is A") 
#IF grade is > .8 THEN
elif grade >= .8 :
    #WRITE B
    print("grade is B") 
#IF grade is > .7 THEN
elif grade >= .7 :
    #WRITE C
    print("grade is C") 
#IF grade is > .6 THEN
elif grade >= .6 :
    #WRITE D
    print("grade is D") 
#ELSE
else:
    #WRITE grade is F
    print("grade is F")
#END-IF
#END
