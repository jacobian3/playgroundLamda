# What is a function? @ 2:16
    # a named block of code
    # that we can call by name
    # pro: they keep 'main body' code to min

# What is scope?



# What is a pure function? @ 10:59
    # a function that doesn't refer to outside vars
    # easiest functions to manage is a pure func.
    # easiest to test

# What happens if assign a function that doesn't return anything?
    # None is returned by default @ 25:45
    # by functions not designed to return ...but you assigne it
    # ex: x = x.append(y) # assigning x.append(y) ret. 'None'

# INTRODUCTION: USER-DEFINED FUNCTIONS
# What are two primary reasons functions are useful?

# REVIEW: FUNCTION ARGUMENT(S)
# Explain aliasing as it relates to funciton aruguments?
# Define Alias? 
    # know person know by another name; stage name

# REVIEW: THE RETURN STATEMENT RETURNS A VALUE
# How do locally defined object escape from a function?

# SUMMARY ARGUMENT TYPES: POSITIONAL AND KEYWORD
# Explain order and requirements of positional and keyword arguments?
    # positional: ea. argument is matched to a variable name in def
    # keyword: args are not required, can be in any order, function def
    # specifies a default value
    #
    # variable positional: any number of positional args can be passed
    # (ie. *arg)
    # variable keyword: any number of keyword key/value can be passed
    # (i.e., **kwargs; usually a dict @ 1:03:40
    # usecase below: 
    #
    # def print_these(*kwargs):
    #     print(kwargs)
    # print_these(this = 'that', other = "another")
    # print_these(zz=[1, 2, 3], yy={'a':1, 'b':2})
    #
    # when mixing positional and keyword argument type, positional
    # must come first

# VARIABLE NAME SCOPING INSIDE FUNCTIONS
# What is a local variable ? @05:25
#   - one that is declared and initialized in a function

# What happens if you try to use a local function outside of the function?
    # @10:18 
    # NameError; 'return' sents back the object bound to the local name
    # Scoping is based on names!!!!
    # review: Variable -> object bound to a name; 'return' of a local var
    # only returns the object. The local name desolves after use; 
    # only the object survives!!!!
    # @ 18:43
    # every time we bind an object to a name we are not copying the object
    # we are just binding it to a name: x = [ 1, 2, 3]
    # y = x (one list is bound to  2 names: x and y)
    # the local variable can't exist outside of the function def
    # however, the object manipulated can! i.e, an appended list can be passed
    # around: this is Aliasing - think stage name

# How are function definitions and global variables similar? @05:30
    # def is simply another variable assignent
    # def is a function object of type <function name>

# What is a global variable? @11:25
   # one that is iniitialized outside a function
   # local and global are about variable names (not objects)

# THE FOUR VARIABLE SCOPES: (L)OCAL, (E)NCLOSING, (G)LOBAL AND (B)UILTINL
# What are the four "naming" scopes within Python?
    # namelookup overides: local > enclosing > global > builtin scope

# SUMMARY EXCEPTION: UNBOUNDLOCALERROR
# If we recieve an UnboundLocalError, what has happened?

# INTRODUCTION: MODULES
# What are modules refered to as libraries? 
# What is a module? How do we call it's attributes, while 
# inside other programs @52:56
    # simply a file with python code
    # the attributes of a module are the global variables of 
    # that file (includes: var and function defs)

# what is the attribute of a module?
    # ex: this.that() # that is a global of module that
    # it is a global variable; this includes functions (they are just vars!!)
    # ie: var = 5 ; is 5 global or local?
    # objects(5) are not global or local; its the (name)space that is scoped


# SUMMARY STATEMENT: IMPORT MODULENAME
# How are modules accessed as attributes?
    # use: from <module name> import <attribute>
# how do we eliminate the module prepend?
    # never!!! from <module name> import * DON'T DO!!!

# SUMMARY STATEMENT: IMPORT MODULENAME AS CONVENIENTNAME
# How can we make the import of modules more convienient?
    # or : import <modlue name> as <convient name>

# SUMMARY STATEMENT: FROM MODULENAME IMPORT VARIABLENAME
# How do we directly import variable names from modules?

#}} SUMMARY: MODULE SEARCH PATH
#Explain options to let Python know about our own module directories?

# SUMMARY: CODING ALL PYTHON SCRIPTS AS MODULES
# What is meant by: 'All Python scripts should be coded as modules'?
# Explain the concept: if __name__ == '__main__': main()

# SUMMARY: RAISING EXCEPTIONS
# Why do we cause exceptions to be raised? What is the advantage of this
# Approach?

# SUMMARY: INSTALLING MODULES
# What are the two main ways to install third-party Python packages?

# FROM THE STANDARD DISTRIBUTION: THE TIME MODULE
# Explain the time module? 

# COMPARING DATETIME OBJECTS
# What primary modules do we use to work with datetime? How are they used? What
# do they do?

# CHANGING A DATE USING THE TIMEDELTA OBJECT
# Explain how timedelta is used to calculate the 
# difference b/t dates?

# 
