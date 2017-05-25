#PROGRAM Ex12DistanceBetweenTwoPointsOnEarth: 
from math import *

#READ first coordinate t_1 and g_1 from user
#READ second coordinate t_2 and g_2 from user 
print "For first point on the earth in degrees"
t_1 = radians(float(raw_input("Enter first number of coordinate pair:\n")))
g_1 = radians(float(raw_input("Enter second number of coordinate pair:\n")))
print "For second point on the earth in degrees"
t_2 = radians(float(raw_input("Enter first number of coordinate pair:\n")))
g_2 = radians(float(raw_input("Enter second number of coordinate pair:\n")))

# test values expressed as decimal degrees
#t_1 = radians(38.898556)
#g_1 = radians(-77.037852)
#t_2 = radians(38.897147) 
#g_2 = radians(-77.043934)
#0.549 is expected distance in km

#CALCULATE distance in kilometers using values expressed as radians 
distance = 6371.01 * acos(sin(t_1) * sin(t_2) 
    + cos(t_1) * cos(t_2) * cos(g_1 - g_2))
#WRITE distance 
print "The distance between points in kilometers is: ", distance

#END Ex12DistanceBetweenTwoPointsOnEarth
