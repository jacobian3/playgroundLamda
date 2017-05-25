#PROGRAM Ex15DistanceUnits.py

#READ # of ft from user
feet = int(raw_input("Enter total number of feet as integer:"))

#SET ft2in = 1 ft is 12 in
#SET ft2yrd = 1 yard is 3 feet 
#SET ft2mile = 5280 feet in one mile
ft2in = 12
ft2yrd = 3
ft2mile = 5280

#COMPUTE as feet times conversion factor
inches = feet * ft2in
yardsF = feet / ft2yrd
yardsB = feet % ft2yrd
milesF = feet / ft2mile
milesB = feet % ft2mile
#WRITE feet and inches as centemeters
#WRITE equivalence in inches
#WRITE equivalence in yards
#WRITE equivalence in miles
print "%s feet is equal to: " % feet
print "%s inches" % inches
print "%s.%s yards" % (yardsF, yardsB)
print "%s.%s miles" % (milesF, milesB)
#END
