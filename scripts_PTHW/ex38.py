# Exercise 38: Doing Things to Lists
# this is a string that will be split into list elements
ten_things = "Apples Oranges Crows Telephine Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# we call on object a function and give it a cammond to split by ''
stuff = ten_things.split(' ') # think split(ten_things,' ')
print "initial state of stuff:", stuff
print "there are %r items" % len(stuff)
# simply another list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", 
    "Boy"] 
print "initial state of more_stuff:", more_stuff
print "there are %r items" % len(more_stuff)

while len(stuff) != 10: # checks for count != 10
    next_one = more_stuff.pop() # transfers elements b/t list
    print "Adding: ", next_one # prompts status to user
    stuff.append(next_one) # adds element to object
    print "stuff is:", stuff
    print "In 'stuff' there are %d items now." % len(stuff)
    print "more_stuff is:", more_stuff
    print "In 'more_stuff' there are %d items now." % len(more_stuff)
    print '*' * 30
    print " "
    

print "There we go: ", stuff # shows user the entire list

print "Let's do some things with stuff."

print "stuff now: ", stuff
print stuff[1] # prints 2nd element of list
print stuff[-1] # print last element of list
# call pop on stuff with no argument
print stuff.pop() # extracts the rightmost element of list 
print "stuff now: ", stuff
# transforms stuff from list to string
# However, this doesn't affect the original list!
# seperates by the object that is given a command by the function '.join()'
print ' '.join(stuff) # call join on ' ' with argument stuff.
print "stuff now: ", stuff
# extracts a slice from 3rd element to 4th(not fifth)
# works like range 
print '#'.join(stuff[3:5])
print "stuff now: ", stuff
