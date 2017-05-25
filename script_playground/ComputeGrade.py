#PROGRAM ComputeGrade
from sys import argv

script, score = argv
print('The script: ', script)
print('The score: ', score)
score = float(score)

def ComputeGrade(score):
    """takes a score as parameter and retursn a grade as a string"""
    #READ score as arg
    #score = float(input("Enter score (0 - 1): "))

    #PROCESS selection of grades and socores
    if score > 0.9:
        grade = 'A'
    elif score > 0.8:
        grade = 'B'
    elif score > 0.7:
        grade = 'C'
    elif score > .6:
        grade = 'D'
    else:
        grade = 'F'
    return grade

answer = ComputeGrade(score)

#WRITE grade as a string
print("A score of %s warrants a grade of %s." % (score, answer))

#END
