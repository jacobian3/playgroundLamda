class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

# print 1, 1, 1
print Parent.x, Child1.x, Child2.x
Child1.x = 2
# print 1, 2, 1
print Parent.x, Child1.x, Child2.x
# print 3, 2, 1 ...I got this wrong; find out why.
Parent.x = 3
print Parent.x, Child1.x, Child2.x
