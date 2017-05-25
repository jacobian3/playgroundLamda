#PROGRAM compute BMI; in python3

#READ heigh and weight from user in lbs
weight = int(input("Enter your weight:\n"))
height = int(input("Enter your height:\n"))

#COMPUTE BMI 
BMI = ( weight ) / ( height * height ) * 703

#WRITE
print ("BMI if %s feet tall & weight %s lbs is %s" % (height, weight,BMI))
#END
