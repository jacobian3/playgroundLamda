import datetime

class TimeStamp(object):

    def __init__(self):
        # now object var 't' is autoset at construction 
        # only get is needed be called
        self.t = str(datetime.datetime.now())

    def get_time(self):
        return self.t

var1 = TimeStamp()
var2 = TimeStamp()

print( var1.get_time() )
print( var2.get_time() )
print()
print( var1.get_time() ) # gets the same time
print( var2.get_time() ) # gets the same time
