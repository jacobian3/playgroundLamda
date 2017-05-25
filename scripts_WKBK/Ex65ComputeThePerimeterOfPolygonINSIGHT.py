#PROGRAM Ex65.py3

from math import *

perimeter = 0

#READ inital x and y coordinates
first_x = float(input("Enter the x part of the coordinate: "))
first_y = float(input("Enter the y part of the coordinate: "))

#SET first values to previous values
prev_x = first_x
prev_y = first_y

#READ remaining coordinates
line = input("Enter the x part of the coordinate (blank to quit)")

#WHILE x is not a space DO
while line != "" :
    #READ y coordinates and convert x part
    x = float(line)
    y = float(input("Enter the y part of the coordinate: (blank to quit)"))

    #COMPUTE and store distance
    distance = sqrt( pow( ( prev_x - x ), 2 ) + \
        pow( ( prev_y - y ), 2 ) )    
    #(5.1)?How does an accumulator work?
    #(5.1)get the current value, add the distance and accumulate it by 
    #storing inside of perimeter
    #(5.1) before you can update the variable you must have already
    #initialized it; see top of program
    perimeter += distance

    #SET first values to previous values for next loop iteration
    prev_x = x
    prev_y = y

    #READ remaining coordinates
    line = input("Enter the x part of the coordinate (blank to quit)")
#ENDWHILE

#COMPUTE and store distance from last point
distance = sqrt( pow( ( first_x - x ), 2 ) + \
    pow( ( first_y - y ), 2 ) )    
perimeter += distance

#WRITE result
print("The perimeter of that polygon is %d." % perimeter)

#END ...TEST (2,3), (2,-1), (-1,-1); answer is 12
