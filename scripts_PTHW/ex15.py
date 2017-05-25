# Exercise 15: Reading Files
# *** this script accepts arguments ***
# import adds the system package to the script
# and it obtains the argv library from the system package
# argv holds the vars passed to the program by the user
from sys import argv

script, filename = argv # argv unpacks held values to variables
# argv takes a parameter and returns a value; set to variable

txt = open(filename) # open creates a file object named 'txt'
# txt isn't the contents of the the file; it is the container that 
# holds the contents of the file

print "Here's your file %r:" % filename # prints the filename to usr

# we call a function on txt named read; '.' gives command 'read' and
# passes to the command and empty parameter; this reads the contents of the
# file object created earlier.
print txt.read() 

print "Type the filename again:"
file_again = raw_input("> ") # raw_input command prompts the user 
# it will assign the standard input to a variable

txt_again = open(file_again) # open function creates a file-object
# the open function takes the parameter and passes it to the file-object

print txt_again.read() # we call on the file-object a method named read.
# the read function has nothing in its parameter. Therefore, we read the the 
# file-object and prints its contents.
