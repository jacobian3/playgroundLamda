##PROGRAM: CenterAStringInTheTerminal (python3)
#
#Center a string of characters within a certain width.
#
# set constant for general width requirements @ 80chrs
# this computation assumes that WIDTH of a std. screen is 80
WIDTH = 80

## Create a new string that wil be centered within a given width when printed.
# @param s: the string that will be centered
# @param width: the width in which the string will be centered.
# @return: a new copy of s that contains the leading spaces needed so that 
# s will appear centered when it is printed.
#ENTERFUNCTION center
def center(s, width):
    #IF the string is too long to center, THEN the original string is returned.
    if width < len(s):
        return s

    #COMPUTE the number of spaces needed and generate the result
    # given that a sentence of arbitrary length is subtracted from the screen
    # what remains is the white space on both sides. In order to get the
    # leading white space (same as ending):we divide total front and back
    # space by 2 choosing and integer result (b/c space can't be a real#).
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result
#ENDFUNCTION

#Demonstrate the center function
# parameters given to be centered to facilite testing 
# CALL center with string RETURNING centered string
#ENTERFUNCTION main
def main():
    print(center("A Famous Story", WIDTH))
    print(center("by:", WIDTH))
    print(center("Someone Famous", WIDTH))
    print()
    print("Once upon a time...") #not centered
#ENDFUNCTION

#CALL main
main()
#END
