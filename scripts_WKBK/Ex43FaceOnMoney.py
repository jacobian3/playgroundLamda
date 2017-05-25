#PROGRAM Ex43.py3

#REPEAT request for proper denomination
name = 0
while True:
    #READ the denomination of note from the user
    prompt = "Enter the denomination of the currency [1,2,5,10,20,50,100]:\n"
    denomination = int(input(prompt))

    #IF denomination is $1 THEN
    if denomination == 1 :
        #SET the name of the individual
        name = "George Washington"

    #IF denomination is $2 THEN
    elif denomination == 2 :
        #SET the name of the individual
        name = "Thomas Jefferson"

    #IF denomination is $5 THEN
    elif denomination == 5 :
        #SET the name of the individual
        name = "Abraham Lincoln"

    #IF denomination is $10 THEN
    elif denomination == 10 :
        #SET the name of the individual
        name = "Alexander Hamilton"

    #IF denomination is $20 THEN
    elif denomination == 20 :
        #SET the name of the individual
        name = "Andrew Jackson"
    
    #IF denomination is $50 THEN
    elif denomination == 50 :
        #SET the name of the individual
        name = "Ulysses S. Grant"

    #IF denomination is $100
    elif denomination == 100 :
        #SET the name of the individual
        name = "Benjamin Franklin"

    #ELSE denomination isn't on the list
    else:
        #ask again the name of the individual
         print("Try again. This denomination doesn't exist in list")
    #ENDIF
    if name != 0:
        break
#UNTIL 
#WRITE name of the individual that appears on the note
print("%s is the name on the note" % name)

#END
