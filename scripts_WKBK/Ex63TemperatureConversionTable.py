#PROGRAM Ex63.py3

#WRITE column headings with correct spacing
#print("Celsius | Fahrenheit") # using eyball of lineup
print("%s\t %s" % ("Celsius","Fahrenheit")) # using formatters

#FOR degree in range 
# range is from [0,100] in incremements of 10
for degree_celsius in range(0,101,10):
    #COMPUTE conversion from celsius to fahrenheit
    degree_fahrenheit = ( degree_celsius * 9 / 5 ) + 32
    #WRITE celsisus, fahrenheit values in 10 degree increments
    print("%5.2f %10.2f" % (degree_celsius, degree_fahrenheit))
#ENDFOR
#END
