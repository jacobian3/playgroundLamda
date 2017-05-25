#PROGRAM Ex51v2.py3 -> PSEUDO for a more refined solution

#SET conversion for letter grade to the number of grade points.
A = 4.0 # since A and A+ have the same value, we can treat them the same way
#so...THINK: this would be similar to f(-2) and f(2) for f(x) = x^2 
A_minus = 3.7
B_plus = 3.3
B = 3.0
B_minus = 2.7
C_plus = 2.3
C = 2.0
C_minus = 1.7
D_plus = 1.3
D = 1.0
F = 0
INVALID = -1

#READ letter grade from user
letter_grade = input("Enter the letter grade [A, A+, A-, etc.]\n")
# we can avoid use of selection structure check by using uppercase()
letter = letter_grade.upper() #changes the case of the letter to prevent logic error

#COMPUTE match for letter grade and grade point
#IF letter is A or A- THEN; NOTE: f(a), f(-a),f(A),etc equal  4.0
#therfore, one condtion will satisfy
    #SET grade point to A value
#IF letter is B+ THEN
    #SET grade point to B+ value
#IF letter is B THEN only one condition is needed
    #SET grade point to B value
#IF letter is B- THEN
    #SET grade point to B- value
#IF letter is C+ THEN
    #SET grade point to C+ value
#IF letter is C THEN
    #SET grade point to C value
#IF letter is C- THEN
    #SET grade point to C- value
#IF letter is D+ THEN
    #SET grade pint to D+ value
#IF letter is D THEN
    #SET grade pint to D value
#IF letter is F THEN
    #SET grade pint to F value
#ELSE
    #SET grade point to INVALID NOTE: this will catch all outside of conditions
#ENDIF
    
#IF grade point is -1 THEN
    #WRITE grade point is not valid
#ELSE
    #WRITE grade point
#ENDIF

#END
