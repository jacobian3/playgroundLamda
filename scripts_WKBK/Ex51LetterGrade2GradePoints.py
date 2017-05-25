#PROGRAM EX51.PY3   

#SET list
A_plus = 4.0
A = 4.0
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
letter_grade = letter_grade.upper()

#COMPUTE match of letter key with numerical value using only selection

#IF letter_grade  == A,a or A+,a+ THEN
if letter_grade == "A" or letter_grade == "A+":
    #SET variable that represents a grade
    gp = A
#IF letter_grade  == A THEN
elif letter_grade == "A-":
    #SET variable that represents a grade gp = A_minus
    gp = A_minus
#IF letter_grade  == B scores THEN
elif letter_grade == "B+":
    #SET variable that represents a grade
    gp = B_plus
#IF letter_grade  == B scores THEN
elif letter_grade == "B":
    #SET variable that represents a grade
    gp = B
#IF letter_grade  == B scores THEN
elif letter_grade == "B-":
    #SET variable that represents a grade
    gp = B_minus
#IF letter_grade  == C scores THEN
elif letter_grade == "C+":
    #SET variable that represents a grade
    gp = C_plus
#IF letter_grade  == C scores THEN
elif letter_grade == "C":
    #SET variable that represents a grade
    gp = C
#IF letter_grade  == C scores THEN
elif letter_grade == "C-":
    #SET variable that represents a grade
    gp = C_minus
#IF letter_grade  == D scores THEN
elif letter_grade == "D+":
    #SET variable that represents a grade
    gp = D_plus
#IF letter_grade  == D scores THEN
elif letter_grade == "D":
    #SET variable that represents a grade
    gp = D
#ELSE SET grade point to invalid
elif letter_grade == "F":
    gp = F
else:
    gp = INVALID
#ENDIF

#WRITE numerical equivalent
#IF gp is not valid THEN
if gp == INVALID:
    print("The numerical grade is invalid")
#ELSE
else:
    #WRITE numerical equivalent
    print("The numerical grade for %s is: %s" % (letter_grade, gp))
#ENDIF
#END
