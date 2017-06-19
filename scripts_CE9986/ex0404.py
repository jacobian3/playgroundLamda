class Square(object):
    def __init__(self):
        """ set attribute """
        self.x = 2

    def squareme(self):
        """ square the int and stroe the value"""
        self.x = self.x**2

    def getme(self):
        """ ret. the integer atribute """
        return self.x

# set var names using constructor
n1 = Square()
n2 = Square()
n3 = Square()
        
n1.squareme()  # from n1 instance get squareme() method; call with self
val1 = n1.getme() # from instance get getme and call w/ self: 
print(val1) # 4

# from inst. get method/call with self
n2.squareme()  #2^2 = 4 
n2.squareme()  #4^2 = 16

val2 = n2.getme() #from instance get getme method and set=2 var
print(val2) # 16
print(n1.getme()) # from n1 inst get getme meth adn set=2: 4

n3.squareme()    # 2^2: 4
n3.squareme()    # 4^2: 16
n3.squareme()    # 16^2: 
n3.squareme()    # 2^2: 
n3.squareme()    # 2^2: big ass number: 4294967296 

val3 = n3.getme() # from n3 get number and set=2: val3
print(val3) #4294967296

print(n1.getme()) #4
print(n2.getme()) #16
print(n3.getme()) #4294967296
