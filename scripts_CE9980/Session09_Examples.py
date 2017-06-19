# DEFAULT KEYWORD ARGUMENTS @ 40:00
def print_these(x=None, y=0, z="YO!"):
    print(x, y, z)

retval = print_these(x=1, y=2, z=3)
print(retval)

# they are optional
# order doesn't matter
print_these(x=1, y=3 ) # prints 3, 0 1 b/c y=0 is default keyword value

# default keyword example using sorted
def sorted(iterable, reverse=False, key=None)

slist = sorted(mylist)
slist = sorted(mylist, reverse=True)
slist = sorted(mylist, key=myfunc)


# POSITIONAL ARGUMENT @ 59:00
# whatever arg we pass becomes
# tuple with ??# of items
def print_these(*arg):
    print(arg)

print_these() 
print_these(2, 3)
print_these(2, 3, 4, 5, 6, 7)
print_these([1, 2, 3], [4, 5, 6], 5, 6)


# EXMAMPLE OF **KWARGS
def print_these(*kwargs):
    print(kwargs)

# whatever arg we pass becomes
# dict with ?# of key/value pairs
print_these() 
print_these(a=5, b=10)
print_these(this="that", other='another')
print_these(zz=[1, 2, 3], yy={'a':1, 'b':2})

# COMBINE POSITIONAL WITH KEYWORD
# positionals must come first!!!
def print_these(arg, x=None, y=0, z="YO!"):
    print(x, y, z)

print_these('xxxxx') # None 0 YO!
