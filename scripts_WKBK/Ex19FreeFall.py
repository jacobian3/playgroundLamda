#PROGRAM Ex19FreeFall.py
from math import *

#SET gravity 
a = -9.8
#READ height from ground
d = float(raw_input("Enter height:\n"))
d = -d # negate the distance b/c it is dropped
#COMPUTE final velocity at impact with the ground
V_f = sqrt(2 * a * d)

#WRITE final velocity 
print "The final velocity is: %s meter per second" % V_f
#END
