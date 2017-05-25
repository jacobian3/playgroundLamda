# Exercise 17: More Files
# *** this script accepts arguments ***
# import adds the system package to the script
# the argv library is imported and used to hold the contents of the arguments 
# also added: package os.path. This library contains the exist method to check
# file existence
from sys import argv 
from os.path import exists

script, from_file, to_file = argv # unpacts arguments to vars

print "Copying from %s to %s" % (from_file, to_file) # print string w/ multi formatter.

# we could do these two on one line, how?
# answer: indata = open(from_file).read()
# this is because module open's parmeter is the argument after the script
# module open creates a file-object
# we call on fileobject 'in_file' {open(from_file)} a read function w/ no param
# this action opens the file in the argument and then reads its contents 
# then assigns those contents to another fileobject
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()


# prints string with formatter formatter
# the formatter is the output of the len module
print "The input file is %d bytes long." % len(indata)

# exist module returns Truth of to_file existence
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input() # waits for user input

#out_file = open(to_file, 'w') # module open creates a file object
#out_file.write(indata) # call on fileobject the write method; 'in_data' passed
open(to_file, 'w').write(indata)
print "Alright, all done."

#out_file.close() # closes both opened file-objects
#in_file.close() # if 'indata = open(from_file).read()' is used, there is never
# an in_file file-object created. therefore, to closeit makes no sense

