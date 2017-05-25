#PROGRAM Ex39SoundLevel.py

#SET noises listed
#if i were to have used a hashtable: items = [<tiems listed>]
jackhammer = 130
gas_lawnmower = 106
alarm_clock = 70
quite_room = 40

#READ decibel level from user
decibel_level= int(input("Enter the decibel level: "))

#IF decibel level is greater than the noises listed THEN
if decibel_level > jackhammer :
    #WRITE that the sound level is more than the loudest noise
    print("noise level is greater than the loudest noise")

#IF decibel level matches the noises listed THEN
elif decibel_level == jackhammer :
    #WRITE listed noise
    print("noise level is the same as a jackhammer")

#IF decibel level matches the noises listed THEN
elif decibel_level == gas_lawnmower :
    #WRITE listed noise
    print("noise level is the same as a gas lawnmower")

#IF decibel level matches the noises listed THEN
elif decibel_level == alarm_clock :
    #WRITE listed noise
    print("noise level is the same as an alarm clock")

#IF decibel level matches the noises listed THEN
elif decibel_level == quite_room :
    #WRITE listed noise
    print("noise level is the same as a quiet room")

#IF decibel level is betwen noises listed THEN
elif jackhammer > decibel_level > gas_lawnmower :
    #WRITE between values
    print("%s is between %s & %s" % (decibel_level, jackhammer, gas_lawnmower))

#IF decibel level is betwen noises listed THEN
elif gas_lawnmower > decibel_level > alarm_clock :
    #WRITE between values
    print("%s is between %s & %s" % (decibel_level, gas_lawnmower, alarm_clock))

#IF decibel level is betwen noises listed THEN
elif alarm_clock > decibel_level > quite_room :
    #WRITE between values
    print("%s is between %s & %s" % (decibel_level, alarm_clock, quite_room))

#IF decibel level is smaller than the noises listed THEN
else:
    #WRITE that the sound level is less than the quietest noise
    print("noise level is less than the quietest noise")

#END
