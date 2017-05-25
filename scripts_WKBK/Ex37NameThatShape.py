#PROGRAM Ex37"".py3

#READ string from the user
number_of_sides = int(input("Enter number of sides of the shape [1-10]:\n"))

#IF 1 THEN
if number_of_sides == 1:
    #WRITE vowel
    print("%s is a line" % number_of_sides)
#IF 2 THEN
elif number_of_sides == 2:
    #WRITE vowel
    print("%s are 2 lines" % number_of_sides)
#IF 3 THEN
elif number_of_sides == 3:
    #WRITE vowel
    print("%s is a triangle" % number_of_sides)
#IF 4 THEN
elif number_of_sides == 4:
    #WRITE vowel
    print("%s is a square" % number_of_sides)
#IF 5 THEN
elif number_of_sides == 5:
    #WRITE vowel
    print("%s is a pentagon" % number_of_sides)
#IF 6 THEN
elif number_of_sides == 6:
    #WRITE vowel
    print("%s is a hexagon" % number_of_sides)
#IF 7 THEN
elif number_of_sides == 7:
    #WRITE vowel
    print("%s is a heptagon" % number_of_sides)
#IF 8 THEN
elif number_of_sides == 8:
    #WRITE vowel
    print("%s is a octagon" % number_of_sides)
#IF 9 THEN
elif number_of_sides == 9:
    #WRITE vowel
    print("%s is a nanagon" % number_of_sides)
#IF 10 THEN
elif number_of_sides == 10:
    #WRITE vowel
    print("%s is a decagon" % number_of_sides)
##ELSE
else:
    #WRITE that the input was invalid
    print("%s is invalid " % number_of_sides)
#END
