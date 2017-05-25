#PROGRAM Ex16AreaAndVolume.py
from math import *

#READ radius, r, from the user
r = int(raw_input("Enter radius as an integer value:\n"))

#COMPUTE area of a circle
A = pi * pow(r,2)
print pi
print pow(r,2)
print A
#COMPUTE volume of a shere
V = ( pi * pow(r,3) * 4 ) / 3
print pow(r,3)
print 4 / 3
print 4 % 3
print ( pi * pow(r,3) * 4 )
print type(pi * pow(r,3) * 4)
#WRITE area of a circle
print "The area of a circle with radius %s is: %s" % (r, A)
#WRITE volume of a sphere
print "The volume of a sphere with radius %s is: %s" % (r, V)
#END
