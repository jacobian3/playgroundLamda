# Exercise 20: Functions and Files:
# import adds the system library and allows access to argv function
# argv holds the arguments of the script
from sys import argv

# argv unpacts script arguments by assigning them to vars
script, input_file = argv

def print_all(f): # function reads data frm file object
    print f.read() # we call on file-object function read(); this line prints all that has been read

# from f get the seek function, and call it with parameters self and 0
# we call a function on file object 'f'; '.' gives command 'seek' w/ parameters 0
def rewind(f): # rewind functions moves file to zero byte in file
    f.seek(0) 

def print_a_line(line_count, f): # reads a line and moves curser after '\n'
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
