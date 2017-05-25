# Ex. 2.03

#WHILE True
while True:
    
    #READ please enter an integer
    line = input("please enter an integer: ")

    #IF input is all digits THEN
    if line.isdigit():
        #WRITE thanks for the integer
        print("THANKS FOR THE INTEGER")
        #BREAK
        break # escape and exit the program
    #ELSE
    else:
        #WRITE  that user didn't enter a valid number
        print("That wasn't an integer.") # loop back to the while test
    #ENDIF
#ENDWHILE
