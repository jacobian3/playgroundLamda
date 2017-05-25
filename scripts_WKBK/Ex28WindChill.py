#PROGRAM py3

#SET
##T_a is air temp in celsius 
##V is wind speed in kilometers per hour

##READ air temperature and wind speed from user
#V = int(input("Enter your wind speed in kilometers:\n"))
#T_a = int(input("Enter your air temperature in celsius:\n"))
#
##COMPUTE 
#wci = 13.12 + 0.6215 * T_a - 11.37 * V + 0.3965 * T_a * V
#wci = int(round(wci))
#
##WRITE
##END


#SET factors for wci 
wc_offset = 13.12
wc_factor1 = 0.6215
wc_factor2 = -11.37
wc_factor3 = .3965
wc_exponent = .16

#READ previous input
temp = int(input("Enter your wind speed in kilometers:\n"))
speed = int(input("Enter your air temperature in celsius:\n"))

#compute wci
wci = wc_offset + \
    wc_factor1 * temp + \
    wc_factor2 * speed ** wc_exponent + \
    wc_factor3 * speed ** wc_exponent

print ("The wind chill is:", round(wci))


