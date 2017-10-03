# @ param string
# @ param width
# @ return is string plus lead characters
def center(string, width=80): # default parameter for normal value
    """ center a string within the screen width """

    # IF width of string is greater that screen, so WRITE string
    if width < len(string):

        return string

    # COMPUTE lead characters needed to display result
    # NOTE: middle of width less the middle of the string is the spacing
    spaces  = ( width - len(string) ) // 2
    
    result = spaces * "-"  + string + spaces * "-"

    return result

def main():
    """ assert test cases """

    print( center("Troy") )
    print( center("My dear lady is a happy camper", 20))
    print( center("My dear lady is a happy camper") )

if __name__ == "__main__":
    main()
