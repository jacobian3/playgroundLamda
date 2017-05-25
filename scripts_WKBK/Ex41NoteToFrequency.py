#PROGRAM Ex41.py3
#?? refine program
from math import *

#READ the name o#READ position from the user
#Seperate the the string into letters and number
note = input("Enter the note[C4, D4, E4, F4, G4, A4, B4, etc.]:\n")
letter = note[0]
number = int(note[-1])

#IF the letter from the user is 'C'
if letter == 'C' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 261.63
        frequency = 261.63
    #ELSE
    else:
        #SET frequency to 261.63
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 261.63
        frequency = frequency / pow(2,(4 - number))

#IF the letter from the user is 'D'
elif letter == 'D' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 293.66
        frequency = 293.66
    #ELSE
    else:
        #SET frequency to 293.66
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 293.66
        frequency = frequency / pow(2,(4 - number))
    #END-IF

#IF the letter from the user is 'E'
elif letter == 'E' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 329.63
        frequency = 329.63
    #ELSE
    else:
        #SET frequency to 329.63
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 329.63
        frequency = frequency / pow(2,(4 - number))
    #END-IF

#IF the letter from the user is 'F'
elif letter == 'F' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 349.63
        frequency = 349.63
    #ELSE
    else:
        #SET frequency to 349.63
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 349.63
        frequency = frequency / pow(2,(4 - number))
    #END-IF

#IF the letter from the user is 'G'
elif letter == 'G' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 392.00
        frequency = 392.00
    #ELSE
    else:
        #SET frequency to 392.00
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 392.00
        frequency = frequency / pow(2,(4 - number))
    #END-IF

#IF the letter from the user is 'A'
elif letter == 'A' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 440.00
        frequency = 440.00
    #ELSE
    else:
        #SET frequency to 440.00
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 440.00
        frequency = frequency / pow(2,(4 - number))

#IF the letter from the user is 'B'
elif letter == 'B' :
    #IF number is 4 THEN
    if number == 4 :
        #SET frequency to 493.88
        frequency = 493.88
    #ELSE
    else:
        #SET frequency to 493.88
        #SET frequency to frequency / 2^(4-x) where x is the number entered
        frequency = 493.88
        frequency = frequency / pow(2,(4 - number))
#END-IF

#WRITE the note's frequency to the user
print("The %s note has a frequency of %s" % (note, frequency))

#END
