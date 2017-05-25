# "None" is frequently used to represent the absence of a value
# therefore, if a values isn't present use: not None => True
# if foo is None:
    # foo is set to None
# if foo is not None:
    # foo is set to something else
def hello(name=None):
    if name == None:
        print('hello, world')
    else:
        print('hello {}'.format(name))

#alternate way to skin cat
def hello2(name="world"): #default to world if nothing entered
    print("Hello {}".format(name))

