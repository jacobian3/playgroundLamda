#PROGRAM Ex40.py3

#READ triangle side length from user
side_one = int(input("Enter integer length of 1st side of the triangle: \n"))
side_two = int(input("Enter integer length of 2nd side of the triangle: \n"))
side_three = int(input("Enter integer length of 3rd side of the triangle: \n"))

#IF side one equals side two and side two equals side three THEN
if side_one == side_two and side_two == side_three :
    #SET name to equilateral triangle
    name = "equilateral"

#IF side one equals side two or side two equals side three or 
#side three equals side one THEN
elif side_one == side_two or side_two == side_three or \
    side_three == side_one :
    #SET name to isoceles
    name = "isoceles"
    
#ELSE
else:
    #SET name to scalene 
    name = "scalene"
#ENDIF

#WRITE name of triangle
print("This is a/an %s triange" % name)
#END

