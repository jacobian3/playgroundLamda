#PROGRAM ""
from math import *

#READ length of side from user
s  = float(raw_input("Enter length of the poloygon side:\n"))
#READ number of sides from the user
n  = float(raw_input("Enter number of sides:\n"))

#COMPUTE area of polygon
area_reg_poly = ( n * s**2 ) / (4 * tan( pi / n ))

#WRITE area of the polygon
print "The area of the polygon is: %0.2f units" % area_reg_poly
#END
