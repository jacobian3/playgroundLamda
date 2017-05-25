#PROGRAM  Ex30.py3
#SET conversion constants
atm2pascal = 0.00000986923267 #is one pascal
mmhg2pascal = 0.00750062 #is one pascal
psi2pascal = 0.000145038 #is one pascal

#READ presure from user in pascals 
pascals = float(input("Enter pressure in pascals:\n"))

#COMPUTE 3 formula from conversion factors
atm = pascals * atm2pascal
mmhg = pascals * mmhg2pascal
psi = pascals * psi2pascal

#WRITE presure in atmospheres, mil of mercury, psi
print("The number of atmospheres is: ", atm)
print("The number of millimeters of mercury is: ", mmhg)
print("The number of pounds per square inch is: ", psi)
#END
