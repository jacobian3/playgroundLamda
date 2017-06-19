class ThisClass(object):
    """ class with one method """
    def report(self):
        """ id's the instance's reference code"""
        print(id(self))

# create three instances using the constructor
a = ThisClass()
b = ThisClass()
c = ThisClass()

a.report()
b.report()
c.report()
print() # blank line
print(id(a))
print(id(b))
print(id(c))

