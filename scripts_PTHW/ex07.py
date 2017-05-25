# Exercise 7: More Printing
# each line prints the a string of the poem; including the formatter
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."

# prints '.' ten times
print "." * 10 # what'd that do?

end1 = "C" # each letter of Cheeseburger is assigned a variable
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# if the comma is removed the concatenated string "Cheese Burger" is written
# as two lines, instead of 2.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
