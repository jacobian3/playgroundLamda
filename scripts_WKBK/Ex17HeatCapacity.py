#PROGRAM Ex17HeatCapacity.py
#READ mass in grams from the user
#READ change in temperature from the user
#SET specific heat capacity as 4.186 (J/g degC)
water_heat_capacity = 4.186 #the specific heat capacity for water
m = float(raw_input("Enter mass of material in grams:\n"))
d_temp = float(raw_input("Enter change in temperature:\n"))

#COMPUTE amount of energy required to increase the temp, q
q = m * water_heat_capacity * d_temp

#WRITE amount of energy
print "The specific head of water is: %s" % water_heat_capacity
print "There are/is %s gram(s) of material" % m
print "The change in temperature is: %s" % d_temp
print "The amount of energy required to cause change is: %s" % q
#END
