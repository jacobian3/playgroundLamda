#PROGRAM ""
from math import *

#READ the sides of of the trangle from the user
s_1 = float(raw_input("Enter side of the triangle:\n"))
s_2 = float(raw_input("Enter side of the triangle:\n"))
s_1 = float(raw_input("Enter side of the triangle:\n"))

##TEST
#s_1 = float(5)
#s_2 = float(5)
#s_3 = float(5)
## expected area is 10.825317547305483

#COMPUTE
#STORE the average of all sides
s = ( s_1 + s_2 + s_3 ) / 2
print s # test simi_perimeter value
#STORE area to formula for area by side length
area = sqrt( s * ( s - s_1) * ( s - s_2 ) * ( s - s_3))

#WRITE the sides to be standard output to 2 decimal precision
print "The area of the triangle is: %0.2f units" % area

#END
