#PROGRAM Ex89CapitalizeIt; python3

#This program takes a string and makes it capitalized

#BEGINFUNCTION: CapitalizeIt
def CapitalizeIt(s):
    #The 'IF'is implicit; char='i' and has space b4 and after THEN #capitalize 
    #This is done, so that string s can be searched and returned with only
    #   characters that fit the pattern replaced (without IF THEN)
    #   result takes the new string without altering the orig
    result = s.replace(" i "," I ")

    #Checks the orginal string (not the altered: result). IF the original isn't
    #   a space, THEN the first char. or the result is capitalized and


    #This is done, in order to always capitalize the FIRST character of the
    #fisrt sentence
    if len(s) > 0:
       #capitalize process
       result = result[0].upper() + \
               result[1 : len(result)]
    #ENDIF

    # this counter is used to advance through the string by len and pos
    pos = 0

    #WHILE we have not gotten to the end of the string DO check
    while pos < len(s): 
        #IF character is '.','?', or '!' and ends a string THEN
        #skip the character.
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            #advance the position of the character one space
            pos = pos + 1
            

            #WHILE we have not gotten to the end of the string && the current
            #character is not space DO 
            while pos < len(s) and result[pos] == " ":
                #advance the position of the character one space
                pos = pos + 1
            #ENDWHILE

            #IF we haen't reached the end of the string THEN
            if pos < len(s):
                #if we have not gotten to the end of the string, but the above
                #condtions have already been meet, then there must be another
                #sentence in the string? We know this because, if we have Capi=
                #talized the first Character, skiped spaces and all special 
                #characters and haven't gotten to the end of a string, then
                #another sentence must exist. Even if the character 
                #has already been capitalized, we will do it again.
                #Since the position of the charcater will be on the first char-
                #acter of the next sentence. we divide the process into 3
                #steps: 1st section is from the beginning to the position of
                #the first character (to but not including) the new position.
                #2nd step is to capitalize the charcacter at the current 
                #position. 3rd step is to attach everyting after this position)
                #that includes one character after the current position to the
                #end of the string. NOTE for the 3rd setion: len() of string
                #count is just like the cardinal 
                #designation. Therefore, total count is always one
                #greater than the total ordinal position available. 
                #(i.e., length of 3 is the index 2 position)
                result = result[0 : pos] + \
                        result[pos].upper() + \
                        result[pos + 1 : len(result)]
            #ENDIF

        #Advance to the next character
        #just because we have capitalized the the first word of the new 
        #sentence, we still must loop through/&advance it to find the end of 
        #this sentence (checking the same condtions as before).
        pos = pos + 1
        #ENDIF
    #ENDWHILE
    #RETURN result string
    return result
#ENDFUNCTION:

#BEGINFUNCTION: Main 
def Main():
    #READ string from user
    string = input("Enter string: ")

    ##test string!!! (Must remove to function)!!!
    string = "what time do i have to be there? what's the address?"
    #CALL CapitalizeIt with user string 
    print("It is capitalized as: ", CapitalizeIt(string) )
#ENDFUNCTION:

#CALL Main() with no parameters
Main()


#END
