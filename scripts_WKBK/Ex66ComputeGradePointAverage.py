#PROGRAM EX66.PY3

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
EXIT = ""

#initialize count and average
#count = 0
#grade_total = 0
all_grades = [] #this method uses len and sum and a list to achieve same end.

#READ letter grade from user
letter_grade = input("Enter the first letter grade [A, A+, A-, etc.]\n")
letter_grade = letter_grade.upper()

#WHILE not sentinel  DO
while letter_grade != EXIT:
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
    else: 
        gp = F
    #ENDIF

    ##COMPUTE and SET summaary of grades and count of grades
    ##1st try i used initialization, counters, and accumulators to est.
    ##average; this required more work
    #count = count + 1
    #grade_total = grade_total + gp
    #average = grade_total / count # accumulates
    
    ##COMPUTE and SET summaary of grades and count of grades
    ##this method uses list to accumulate, get length, and average
    all_grades.append(gp)
    average = sum(all_grades) / len(all_grades)

    #READ input and check for sentinel value
    print("Get average of a all values by leaving blank and pressing ENTER")
    letter_grade = input("Enter the letter grade [A, A+, A-, etc.]\n")
    letter_grade = letter_grade.upper()
#ENDWHILE

#WRITE numerical equivalent
    #print("The numerical average for the %s grades is: %s" % (count, average))
    print("The numerical average for: %s is %s" % (all_grades, average))
#END
