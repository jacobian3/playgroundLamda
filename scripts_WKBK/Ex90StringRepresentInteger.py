#Determine if string is an integer
#@param s is string to check
#@return: integer -> T, else -> F bool
def isInteger(s):
    #so that whitespace is stripped away from the s parameter
    #strips from beginning and end
    s = s.strip()

    #checks if 1st character is +,-, combined with digit
    #this is to capture the situaitons where the first condition is False (+/-)
    #however one or more chaacters are digits (the most common case)
    #second selection statement check to see if only one char. exist and that
    #character is a digit. Both cases return True / Else is not a digit and 
    #consequently false
    #method isdigit returns T/F based on evaluation of 1 character as digit.
    #the slicing of the string allows me to check just characters to the right 
    #of a +/-
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

#ENTERFUNCTION main
def main():
    #input taken from user and assigned
    s = input("Enter a string: ")
    #True prints string existance
    if isInteger(s):
        print("That sring represents an integer.")
    else:
        print("That string does not represent an integer.")
#ENDFUNCTIOIN

# the name variable is assigned to __main__, which calls the main function

if __name__ == "__main__":
    main()
