#PROGRAM Ex29.py3

#SET constants
F_constant1 = 9 / 5 
F_constant2 = 32
K_constant = 273.15

#READ temperature in F
temp_in_c = int(input("Enter your temperature reading:\n"))

#COMPUTE C and K
Fahrenheit = temp_in_c * F_constant1 + F_constant2
Kelvin = temp_in_c + K_constant

#WRITE temperature in C and K
print("The temperature in degree Fahrenheit is: ", Fahrenheit)
print("The temperature in degree Kelvin is: ", Kelvin)

#END
