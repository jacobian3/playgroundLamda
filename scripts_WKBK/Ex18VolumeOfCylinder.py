#PROGRAM Ex18VolumeOfCylinder.py
from math import *

#READ radius of cylinder from user
#READ height of cylinder from user
r = float(raw_input("Enter radius of cylinder:\n"))
height = float(raw_input("Enter height of cylinder:\n"))

#COMPUTE volue of a cylinder
A_cylinder = 2 * pi * r**2
V_cylinder = height * A_cylinder

#WRITE Volume rounded to one decimal place
#note how the formatter is at 1 decmal precision
print "The volume of a cyliner of"
print " height: %s and radius: %s is: %0.1f" % (height, r, V_cylinder )
#END
