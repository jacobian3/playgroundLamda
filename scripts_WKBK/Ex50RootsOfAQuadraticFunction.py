#PROGRAM Ex50.py3
from math import *

#READ input a b and c from user
a = int(input("Enter the value for 'a':\n"))
b = int(input("Enter the value for 'b':\n"))
c = int(input("Enter the value for 'c':\n"))

#COMPUTE the discriminent
discriminent =  b**2 - 4 * a * c 

#IF discriminent is less than zero THEN
if discriminent < 0 :
    #SET root_1 = 'no real'
    root_1 = 'not real'
    #SET root_2 = 'no real'
    root_2 = 'not real'
#IF discriminent is equal to zero THEN
elif discriminent == 0 :
    #SET root_1 = - b / 2a
    root_1 = - b / 2 * a
    #SET root_2 = 'no real'
    root_2 = 'not real'
#ELSE discriminent is greater than zero THEN
else:
    #SET root_1 = - b + root( b**2 - 4 * a * c ) / 2a
    root_1 = (- b + sqrt( b**2 - 4 * a * c )) / 2 * a
    #SET root_2 = b + sqrt( b**2 - 4 * a * c ) / 2 * a
    root_2 = (b + sqrt( b**2 - 4 * a * c )) / 2 * a
#END-IF

#WRITE the root 
print("The discriminent is: %s" % discriminent)
print("Root 1 is %s and root 2 is %s" % (root_1, root_2))
#end
