#PROGRAM Ex04AreaOfAField:
#READ field length as float
field_length = float(raw_input("What is the field length[in feet]?\n"))
#READ field height as float
field_height = float(raw_input("What is the field height?[in feet]\n"))
#CALCULATE field area in feet
field_area = field_height * field_length
#CALCULATE field area in acres
SQFT_PER_ACRE = 43560 # convesion constant
field_acre = field_area / SQFT_PER_ACRE
#WRITE field area in feet
print "The field area is: ",field_acre," acres"
#END
