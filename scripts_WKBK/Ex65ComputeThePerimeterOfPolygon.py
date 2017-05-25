#PROGRAM Ex66.py3

from math import *

perimeter = 0

#READ inital x and y coordinates
first_x = float(input("Enter the x part of the coordinate: "))
first_y = float(input("Enter the y part of the coordinate: "))

#SET first values to previous values
prev_x = first_x
prev_y = first_y

#WHILE x or y is not a space DO
    #READ inside of loop x and y coordinates
    second_ = float(input("Enter the x part of the coordinate: (blank to quit)"))
    y2 = float(input("Enter the y part of the coordinate: (blank to quit)"))

    #COMPUTE and store distance
    distance = math.sqrt( math.pow( ( x2 - x1 ), 2 )+ \
        math.pow( ( y2 - y1 ), 2 ) )    
    perimeter += distance

    #READ inside of loop x and y coordinates
    x1 = float(input("Enter the x part of the coordinate: (blank to quit)"))
    y1 = float(input("Enter the y part of the coordinate: (blank to quit)"))
#ENDWHILE

#WRITE
print("The perimeter of that polygon is %d." % perimeter)

#END ...TEST (2,3), (2,-1), (-1,-1); answer is 5
