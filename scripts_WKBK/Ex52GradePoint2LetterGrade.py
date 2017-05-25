#PROGRAM Ex52.py3

#READ
number_grade = float(input("Enter grade for the student: "))

#COMPUTE letter grade 
#IF number grade is 4.0 or greater THEN

if number_grade >= 4.0 :
    #SET letter grade to A
    letter_grade = 'A'
elif number_grade >= 3.3 :
    letter_grade = 'B+'
elif number_grade >= 3.0 :
    letter_grade = 'B'
elif number_grade >= 2.7 :
    letter_grade = 'B-'
elif number_grade >= 2.3 :
    letter_grade = 'C+'
elif number_grade >= 2.0 :
    letter_grade = 'C'
elif number_grade >= 1.7 :
    letter_grade = 'C-'
elif number_grade >= 1.3 :
    letter_grade = 'D+'
elif number_grade >= 1.0 :
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("%s has letter grade: %s" % (number_grade, letter_grade))
#END]
