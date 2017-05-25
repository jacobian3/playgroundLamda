#PROGRAM Ex68py3: compute the parity bits using loops

#READ bits from the user
#READ to the user that "" is the sentinel
line = input("Enter 8 bits(space to finish)")

#WHILE not sentinel DO
while line != "":
    #IF line in not 8 characters long or count of characters isn't 8 THEN 
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        #WRITE to the user to try again with correct entry
        print("That wasn't 8 bits...try again")
    #ELSE
    else:

        #SET ones <- # of 1's 
        ones = line.count("1")

        #IF # of 1's is even THEN
        #let ones mod 2 is zero
        if ones % 2 == 0:
            #WRITE that the even bit is "0"
            print("The parity bit should be 0.")
        #ELSE
        else:
            #WRITE that the odd bit is "1"
            print("The parity bit should be 1.")
        #ENDIF
    #ENDIF

    #READ bits from the user
    #READ to the user that "" is the sentinel
    line = input("Enter 8 bits(space to finish)")
#ENDWHILE
#END

