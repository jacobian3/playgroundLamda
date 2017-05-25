#PROGRAM Ex11FuelEfficiency

#READ value from user in American units
au = float(raw_input("What is fuel efficiency in (MPG)\n"))

#CALCULUATE conversion for (MPG) -> (L/100 km)
#SET conversion factor for use
conversion = 13.5 / 21
miles_2_liters = au * conversion

#WRITE equivalent value in Canadian units
a =  "Fuel efficiency of %s (MPG) in Canadian" % au
b =" units is %s (L/100 km)" % miles_2_liters
print a + b
#END Ex11FuelEfficiency
