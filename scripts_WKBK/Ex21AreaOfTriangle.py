#PROGRAM Ex21AreaOfTriangle.py

#READ base of triangle from user
#READ height of triangle from user
height = float(raw_input("Enter height of the triangle:\n"))
base = float(raw_input("Enter base of the triangle:\n"))

#CALCULATE area of trangle using standard formula
area_of_trangle = ( height * base ) / 2
#WRITE the area of the triange 
print "The area of the triangle is: %s units" % area_of_trangle
#end
