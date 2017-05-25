class ThisClass(object):
    def report(self): # self in the method is the instance object called
        print(id(self)) # self = x

a = ThisClass() # self called implicitly, as first argument
# 
a.report()

b = ThisClass()
b.report()

c = ThisClass()
c.report()

print(id(a))
print(id(b))
print(id(c))

