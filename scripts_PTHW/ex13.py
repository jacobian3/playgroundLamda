# Exercise 13: Parameters, Unpacking, Variables
# *** this script accepts arguments ***
# import statement adds the system library, planned for use, to the script
# argv holds arguments, passed to python, at runtime
from sys import argv

script, first, second, third = argv # unpacts argv to respective vars

print "The script is called:", script # prints the arg variables
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
