#PROGRARM Ex45.py3

#READ position from the user
position = input("Enter the positon on the chess board [a1, e6, etc]:\n")
#Seperate the the string into letters and number
letter = position[0]
number = int(position[1])

#COMPUTE color of square
#Use even or odd position modulus to determine position
#IF leter is a, c, e, or g THEN
if letter == 'a' or \
    letter == 'c' or \
    letter == 'e' or \
    letter == 'g' :
    #IF number is even THEN
    if number % 2 == 0 :
        #SET the color will be white
        color = 'white'
    #ELSE
    else:
        #SET the color will be black
        color = 'black'
    #END-IF
#IF leter is b, d, f, or h THEN
elif letter == 'b' or \
    letter == 'd' or \
    letter == 'f' or \
    letter == 'h' :
   #IF number is even THEN
    if number % 2 == 0 :
        #SET the color will be black
        color = 'black'
    #ELSE
    else:
        #SET the color will be white
        color = 'white'
    #END-IF

#WRITE the color of the position
print("The position %s has a color of %s." % (position, color))
#END

