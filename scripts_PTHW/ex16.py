# Exercise 16: Reading and Writing Files
# *** this script accepts arguments ***
# import adds the system package
# the system package contains the argv library
from sys import argv 

# argv unpacks the arguments (It assigns them to vars).
script, filename = argv

print "We're going to erase %r." % filename # prints string with formatter
print "If you don't wan't, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # prompt user for standard input

print "Opening the file..." # prompts user to status
target = open(filename, 'w') # function open creates a file object which
# contains the file name

print "Truncating the file. Goodbye!"
# we call on the fileobject a function truncate that, without parameters,
# empties the existing file.
target.truncate()

print "Now I'm going to ask you for three lines."
# prompts standard input and makes assignment
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# call on file object a method called write; var contents are respectively
# written to the file object by the function.
target.write(line1)
target.write("\n") # creates a new line after each variable write to file
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() # function close() closes file object:target
