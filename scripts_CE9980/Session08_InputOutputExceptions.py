#---------------------- FILE, DIRECTORY AND EXTERNAL PROGRAM I/O; EXCEPTIONS

# INDEXERROR WITH SYS.ARGV (WHEN USER PASSES NO ARGUMENT)
# when using sys.argv, what happens when the user passes no argument?
    # sys module
    # program ask for items not avail
# x

# WRITING AND APPENDING TO FILES USING THE FILE OBJECT
# When we need to open or append a file how do we do it?
    # file write() method
    # explicit newlines
    # we can use "with" to avoid having to close the file
# x
        
# SUMMARY TASK: REDIRECTING THE STDOUT DATA STREAM
# Why do we call it the 'output pipe' from our program?
    # conduit
    # i.e.,any print statemen
    # redirection operator STDIN; '<' ; cat < file
    # redireciton operator STDIN; '|' ; ls -l | xx.py (from programs)
    # redirection operator STDOUT; '>' ; ls > file(for files)
    # redirection operator STDOUT; '|' ; STDOUT -> STDIN(for programs)

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
# x

# SUMMARY TASK: WRITING TO STDOUT IN DIFFERENT WAYS
# What three ways can we write to STDOUT?
# x

# SUMMARY TASK: READING AND REDIRECTING THE STDIN DATA STREAM
# why do we call the 'input pipe' to our program?
# In what ways do we pipe data into our program?
# x

# SUMMARY TASK: READ DIRECTORIES WITH OS.LISTDIR()
# What are the functions employed in order to read a directory?
    # os.listdir(path) 
# How does os.path.join() help with this?
    # NOTE:
    # The os.path.join() function is helpful if you need to create strings for 
    # filenames.
    # os.path.sep ; returns correct seperator for  operating sys ('/') ('\')
    # backslash on Windows and Forward Slash on OS X and Linux

    # HANDLING ABSOLUTE AND RELATIVE PATHS
    # os.path.abspath(path)
    # os.path.isabs(path)
    # os.path.relpath(path, start) ; <path> folder ->  ../<start> (the last '/')
    # os.path.dirname(path)
    # os.path.basename(path)
    # *os.path.split() - ... 
    # *os.path.join() - ... is helpful if y need to create strings for filenames
# x

#THE CURRENT WORKING DIRECTORY
# How can you can get/change the current working directory as a string value?
    # the os.getcwd() function and change it with os.chdir().
    # *the os.chdir() changes
# x

# CREATING NEW FOLDERS WITH OS.MAKEDIRS();(ATBS, files)
# how do you make a new directory?
    # os.makedirs()
# x

# SUMMARY TASK: READ DIRECTORY LISTING TYPE WITH OS.PATH.ISFILE() AND 
# OS.PATH.ISDIR()
# What methods are used to distinguish a file from a directory? 
    # CHECKING PATH VALIDITY
    # os.path.exists(path) - path/file existance
    # os.path.isfile(path)
    # os.path.isdir(path)
# x

# SUMMARY TASK: READ FILE SIZE WITH OS.PATH.GETSIZE()
# What do we need to do in order to read file size?
    # os.path.getsize(path)
# x

# SUMMARY EXCEPTION: OSERROR WITH OS.LISTDIR() (AND A BAD DIRECTORY)
# What will happen if we try to read from a directory that doesn't exist?
# How do we handle this situation?
# x

# SUMMARY MODULE: LAUNCH AN EXTERNAL PROGRAM WITH SUBPROCESS
# What module is imorted to create a subprocess?
# What do subprocesses allow us to do?
    # keyword arguments 
    # stdin= (the standard input stream: default keyboard)
    # stdout= (standard output stream: default screen)
    # stderr= (standard error output stream: default screen) 
# x

# SIDEBAR -- SUMMARY FUNCTION: TRAVERSE A DIRECTORY TREE WITH OS.WALK())
# What is so 'magical' about traversing a tree with python?
# How does the process occour?
# x

# SUMMARY TASK: READING AND REDIRECTING THE STDIN DATA STREAM
# 3 DATA STREAMS IN UNIX / WINDOWS
# process: a running program
#     - has a PID (process ID)
#     - allocates memory with permission of the OS
#     - writes to STDOUT and/or STDERR
#     - may read from STDIN
#     - may read/write to files(the disk)
#     - may make a network connection (over socket)
# x
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
