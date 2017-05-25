# Ex.2.7

#SET counter to 1
counter = 1

times  = input("how many times should I greet you?: ")

if not times.isdigit():
    #indicate error that let to exit
    #it's undesirable to get chrs that aren't digits
    #therefore, we create error checking
    exit('error: please enter an integer')

times = int(times) # done after .isdigit b/c AttributeError

#WHILE counter is <= times:
while counter <= times:
    #WRITE message to user
    print("Happy birthday to you! time:{}".format(counter))
    #increment counter
    counter += 1
