#---------------------- FILE, DIRECTORY AND EXTERNAL PROGRAM I/O; EXCEPTIONS

# INDEXERROR WITH SYS.ARGV (WHEN USER PASSES NO ARGUMENT)
# when using sys.argv, what happens when the user passes no argument?

# WRITING AND APPENDING TO FILES USING THE FILE OBJECT
# When we need to open or append a file how do we do it?
        
# SUMMARY TASK: READING AND REDIRECTING THE STDOUT DATA STREAM
# SUMMARY TASK: REDIRECTING THE STDOUT DATA STREAM
# What do we call the 'output pipe' from our program to the os?
# What three ways can we 'pipe' the output to onother program?

# SUMMARY TASK: WRITING TO STDOUT IN DIFFERENT WAYS
# what do we call the 'input pipe' to our program (usually the keyboard)?

# SUMMARY TASK: READ DIRECTORIES WITH OS.LISTDIR()
# What are the functions employed in order to read a directory?
# How does os.path.join() help with this?
# NOTE:
# os.path.join(): Backslash on Windows and Forward Slash on OS X and Linux
# The os.path.join() function is helpful if you need to create strings for 
# filenames.

# SUMMARY TASK: READ DIRECTORY LISTING TYPE WITH OS.PATH.ISFILE() AND 
# OS.PATH.ISDIR()
# What methods are used to distinguish a file from a directory?

# SUMMARY TASK: READ FILE SIZE WITH OS.PATH.GETSIZE()
# What do we need to do in order to read file size?

# SUMMARY EXCEPTION: OSERROR WITH OS.LISTDIR() (AND A BAD DIRECTORY)
# What will happen if we try to read from a directory that doesn't exist?
# How do we handle this situation?

# SUMMARY MODULE: LAUNCH AN EXTERNAL PROGRAM WITH SUBPROCESS
# What module is imorted to create a subprocess?
# What do subprocesses allow us to do?

# FORKING CHILD PROCESSES WITH MULTIPROCESSING
# What is forking? What situations is it used?

# SIDEBAR -- SUMMARY FUNCTION: TRAVERSE A DIRECTORY TREE WITH OS.WALK())
# What is so 'magical' about traversing a tree with python?
# How does the process occour?

# SUMMARY TASK: READING AND REDIRECTING THE STDIN DATA STREAM
# 3 DATA STREAMS IN UNIX / WINDOWS
# process: a running program
#     - has a PID (process ID)
#     - allocates memory with permission of the OS
#     - writes to STDOUT and/or STDERR
#     - may read from STDIN
#     - may read/write to files(the disk)
#     - may make a network connection (over socket)

# STDIN (the standard input stream: default keyboard)
# STDOUT (standard output stream: default screen)
# STDERR (standard error output stream: default screen) 

# === write STDOUT to a file with '>' === 
# 
# $ myprog > myfile.txt
# 
# 
# === append STDOUT to a file with '>>' === 
# 
# $ myprogram >> myfile.txt
# 
# === pipe STDOUT to another program's STDIN with '|' ===
# 
# $ myprog | otherprog
# 
# === direct contents of a file to STDIN '<'
# 
# $ myprog < myfile.txt

# @24:22
import os

for item in os.listdir('/'):
    print('entry: ' + item)
    if os.path.isfile(item):
        print(os.path.getsize(item))
# SYS.ARGV

# 3 DATA STREAMS IN UNIX / WINDOWS
# process: a running program
#     - has a PID (process ID)
#     - allocates memory with permission of the OS
#     - writes to STDOUT and/or STDERR
#     - may read from STDIN
#     - may read/write to files(the disk)
#     - may make a network connection (over socket)

# STDIN (the standard input stream: default keyboard)
# STDOUT (standard output stream: default screen)
# STDERR (standard error output stream: default screen) 

# === write STDOUT to a file with '>' === 
# 
# $ myprog > myfile.txt
# 
# 
# === append STDOUT to a file with '>>' === 
# 
# $ myprogram >> myfile.txt
# 
# === pipe STDOUT to another program's STDIN with '|' ===
# 
# $ myprog | otherprog
# 
# === direct contents of a file to STDIN '<'
# 
# $ myprog < myfile.txt

# @24:22
import os

for item in os.listdir('/'):
    print('entry: ' + item)
    if os.path.isfile(item):
        print(os.path.getsize(item))
# SYS.ARGV

------------------------------------Exceptions

# INTRODUCTION: EXCEPTIONS
# What is an exception? 
# What are the two types of errors? Which one is handled with an exception?

# SUMMARY: EXCEPTIONS SIGNIFY AN ERROR CONDITION
# When is an exception raised?
# Name the 4 different types of anticipateable errors?

# SUMMARY STATEMENTS: TRY BLOCK AND EXCEPT BLOCK
# How to avoid an anticipatable exception?
# Explain the try and exception blocks?

# SUMMARY TECHNIQUE: TRAPPING MULTIPLE EXCEPTIONS
# SUMMARY TECHNIQUE: CHAINING EXCEPT: BLOCKS
# How do we trap multiple exeptions? What are the two methods employed?

------------------------------------ ATBS notes
#THE CURRENT WORKING DIRECTORY
# You can get the current working directory as a string value with 
# the os.getcwd() function and change it with os.chdir().

# CREATING NEW FOLDERS WITH OS.MAKEDIRS()

# HANDLING ABSOLUTE AND RELATIVE PATHS
os.path.abspath(path)
os.path.isabs(path)
os.path.relpath(path, start)

# FINDING FILE SIZES AND FOLDER CONTENTS
os.path.getsize(path)
os.listdir(path) 

# CHECKING PATH VALIDITY
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)




