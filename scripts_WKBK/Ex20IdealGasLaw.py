#PROGRAM Ex20IdealGasLaw.py
#SET ideal gas constant @ 8.314 J / (mole * K)
R = 8.314

#READ the volume of the container
#READ presure of the container from the user
print "this program will provide the amount of moles of gas in a SCUBA tank"
V = float(raw_input("Enter the volume in liters:\n"))
P = float(raw_input("Enter the pressure in Pascals:\n"))
C = float(raw_input("Enter the temperature in degrees celsius:\n"))
T = C + 273.15 #SET Celcius to Kelvin converter

##TEST known values
#R = 0.08206 #Liter * atm * mol^-1 * K^-1
#V = 18.6 #Liters
#P = 2.35 #atm
#T = 293.15 #Kelvin
## n should be 1.8173625713427455

#COMPUTE the amount of gas in moles using PV = nRT
n = ( P * V ) / ( R * T )

#Why does this provide a wrong result?
#n2 = P * V / R * T  # WTF ?? 

#WRITE the amount of gas in moles 
print "The amount of gas in moles is %s" % n
#END
