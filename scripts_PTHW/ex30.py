# Exercise 30: Else and If
# assign values to vars
people = 30 
cars = 40
trucks = 15

# if (alone) test all conditions
# if / elif / else test only as many conditions that as needed
if cars > people:
    print "We could take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print  "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
