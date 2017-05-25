#PROGRAM Ex60py
import random

#SET red and green spaces because they are specific
red_spaces = [
    1, 3, 5, 7, 9, 12,
    16, 18, 19, 21, 23, 25,
    27, 30, 32, 34, 36, 14]

green_spaces = [0,37]

#COMPUTE dice roll from 0 - 37; 37 = 00
spin = random.randint(0,37)

##TEST for limited choices
#choices = [0, 13, 37]
#spin = random.choice(choices)

#WRITE spin result
print "The spin resulted in %d ..." % spin

#IF spin is 0 THEN
if spin == 0 :
    #SET Pay to 0
    print 'Pay 0'
#IF spin is 37 THEN
elif spin == 37:
    #SET Pay to 00
    print 'Pay 00'
#ELSE
else:
    #COMPUTE bet logic
    #IF single number THEN
    if spin >= 1 and spin <= 36 :
        #SET Pay to single number 
        print "Pay ", spin
    #ELSE
    else:
        print ""
    #ENDIF

    #IF spin is one of the red spaces THEN
    if spin in red_spaces :
        #SET Pay to red
        print 'Pay Red'
    #IF spin is one of the green spaces THEN
    elif spin in green_spaces :
        #SET Pay to green
        print 'Pay Green'
    #ELSE
    else:
        #SET Pay to black
        print 'Pay Black'
    #ENDIF

    #IF spin is Even THEN
    if spin % 2 == 0 :
        #SET Pay to Even
        print 'Pay Even'
    #ELSE spin is Odd THEN
    else:
        #SET Pay to odd
        print 'Pay Odd'
    #ENDIF

    #IF spin is between 1 and 18 THEN
    if spin >= 1 and spin <= 18 :
        #SET Pay to 1 to 18
        print 'Pay 1 to 18'
    #ELSE
    else:
        #SET Pay to 19 to 36
        print 'Pay 19 to 36'
    #ENDIF
#ENDIF
