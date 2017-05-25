#PROGRAM Ex55.py

#SET names to frequency 
#use format: [0-9].[0-9]e[0-9] or [0-9].[0-9]E[0-9]
gamma_rays = 3e19
x_rays = 3e17
ultraviolet_light = 7.5e14
visible_light = 4.3e14
infrared_light = 3e12
microwaves = 3e9

#READ frequency of radiation from user
radiation_frequency = float(input("Enter frequency of radiation: "))

#COMPUTE match
#IF frequency range greater or equal to freq. range value THEN
if radiation_frequency >= gamma_rays :
    #SET frequency_name
    frequency_name = "Gamma rays"

#IF frequency range greater or equal to freq. range value THEN
elif radiation_frequency >= x_rays :
    #SET frequency_name
    frequency_name = "X-rays"

#IF frequency range greater or equal to freq. range value THEN
elif radiation_frequency >= ultraviolet_light :
    #SET frequency_name
    frequency_name = "Ultraviolet Light"

#IF frequency range greater or equal to freq. range value THEN
elif radiation_frequency >= visible_light :
    #SET frequency_name
    frequency_name = "Visible light"

#IF frequency range greater or equal to freq. range value THEN
elif radiation_frequency >= infrared_light :
    #SET frequency_name
    frequency_name = "Infrared light"

#IF frequency range greater or equal to freq. range value THEN
elif radiation_frequency >= microwaves :
    #SET frequency_name
    frequency_name = "Microwaves"

#ELSE 
else:
    #SET frequency_name
    frequency_name = "Radio waves"
#ENDIF

#WRITE frequency_name 
print("%s is in the %s range." % (radiation_frequency, frequency_name))

#END
