## Emulates do-while in Python
#i = 1           # init

#while True:
#    print(i) 
#	i += 1      # update
#	if i > 3:   # test condition
#		break

#REPEAT 
while True:
    #READ the month from the user
    month = int(raw_input('Please enter the month [1-12]: '))

    #UNTIL month is not within range [1,12]
    if not(month < 1 or month > 12):
        break
