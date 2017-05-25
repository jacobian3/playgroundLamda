#understand looping structure:

#Remember: ordinal == ordered, 1st; cardinal == cards at random
# animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']]
# in this example 'bear' is the first; not zeroth element

def where_number(max):
    i = 0
    # note: before you can loop over any collection with a for-loop, there must
    # be a place to store the result of the list first. 
    #This takes the form of an empty list
    #To build a list, start with an empty list
    numbers = [] #this list is a colection of ordered things

    # this while loop can iterate of over an an infinite posibiliy set
    while i < max : # this condition ensures that the loop eventually terminates
        print "At the top i is %d" % i
        numbers.append(i) # append addds a new element to the end of a list
                          # in this case number contains the collection of 
                          # ordered elements

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The number: "

    # this for-loop can only iterate over a colection of things
    # the variable num is initialized when the for-loop starts;
    # it is initialized to the curent element on each iteration
    for num in numbers: # if you had used range(), it would have done numbers
        print num       # fist to last, not including the last

value = int(input("Please Enter a maximum value:"))
where_number(value)
