#PROGRAM Ex14HeightUnits:

#READ # of ft from user
#READ # of in from user
feet = int(raw_input("Enter total number of feet as integer:"))
inches = int(raw_input("Enter total number of inches as integer:"))

#SET ft2in = 1 ft is 12 in
#SET in2cm = 1 in is 2.54 cm
ft2in = 12
in2cm = 2.54

#CALCULATE in_total = ft * ft2in + in
#CALCULATE cm = imperial in inches * in2cm
inches_total = feet * ft2in + inches
cm = inches_total * in2cm

#WRITE feet and inches as centemeters
print "%s feet and %s inches are equal to %s centimeters" % (feet, inches, cm)
#END Ex14HeightUnits 
