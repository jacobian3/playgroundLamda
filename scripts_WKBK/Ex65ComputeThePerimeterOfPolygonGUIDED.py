#PROGRAM EX66.PY3

from math import *

#store the perimeter of the polygon
#think of this as storing the entire perimeter of the polygon. Coincidentally
#the whole perimeter at this point is zero 
perimeter = 0

#READ inital x and y coordinates
# notice that the values are read in as type float
# this will later be important. When the looping for subsequent points begins
# the x value must be a float, so that "" can be read
first_x = float(input("Enter the x part of the coordinate: "))
first_y = float(input("Enter the y part of the coordinate: "))

#SET first values to previous values
#this converts first to previous, so that your equation willl always have a
#previous x (x_1, y_1) value.
#this also stores the first_x and first_y values for use at the end to close
#the polygon. This exchange is like a movement
prev_x = first_x
prev_y = first_y

#READ remaining coordinates
#check for sentinel value before entering the loop
#no need to check for y value because its existance is undestood to be implied 
#by the x value NOTE "line" is a string 1st, then is subjected to the condition
#to check for sentinel. It isn't until it is inside of the loop that it becomes
#a float value
print("You must enter at least one other point")
line = input("Enter the x part of the coordinate (blank to quit)")

#WHILE x is not sentinel DO
while line != "" :
    #READ y coordinates and convert x part
    #convert (x and y) to float for calculation
    x = float(line)
    y = float(input("Enter the y part of the coordinate: (blank to quit)"))
    #??why will this not work??
    #x = float(input("Enter the x part of the coordinate (blank to quit)"))

    #COMPUTE and accumulate distance
    # this distance equation is tricky. normally ...
    print("")
    print("@BEGIN prev_x=", prev_x, "prev_y=", prev_y, "x=", x, "y=", y) #DBUG
    #distance = sqrt( pow( ( prev_x - x ), 2 )+ \
    #    pow( ( prev_y - y ), 2 ) )    
    #THIS WAY IS WRITTEN AS THE FORMULA 
    distance = sqrt( pow( ( x - prev_x ), 2 )+ \
        pow( (y - prev_y ), 2 ) )    
    print("distance after calc: ", distance)#DBUG
    print("perimeter before accumulation:", perimeter)#DBUG
    perimeter += distance
    print("perimeter after accumulation:", 
        perimeter, "distance:", distance)#DBUG

    #SET first values to previous values for next loop iteration
    #after each calculation we move to the next by exchanging current value and
    #previous values
    prev_x = x
    prev_y = y
    print("@END prev_x=", prev_x, "prev_y=", prev_y, "x=", x, "y=", y)#DBUG

    #READ remaining coordinates
    line = input("Enter the x part of the coordinate (blank to quit)")
#ENDWHILE

#COMPUTE and store distance from last point and connect with first point
# a seperate calculation has to be done because we are getting the distance
#from the last point of the polygon and finding its distance to the first point
print("")
print("@BEGIN prev_x=", prev_x, "prev_y=", prev_y, "x=", x, "y=", y) #DBUG
print("first_x:", first_x, "first_y", first_y)
#distance = sqrt( pow( ( first_x - x ), 2 )+ \
#    pow( ( first_y - y ), 2 ) )    
# THIS WAY IS WRITTEN AS THE FORMULA 
distance = sqrt( pow( ( x - first_x ), 2 ) + \
    pow( ( y - first_y), 2 ) )                
print("distance after calc: ", distance)#DBUG
print("perimeter before accumulation:", perimeter)#DBUG
perimeter += distance
print("perimeter after accumulation:", perimeter, "distance:", distance)#DBUG

#WRITE result
print("The perimeter of that polygon is %d." % perimeter)

#END ...TEST (2,3), (2,-1), (-1,-1); answer is 12
