import datetime

class TimeStamp(object):
    """ store the current timestamp in an instance"""
    def __init__(self):
        self.t = str(datetime.datetime.now()) # t is attribute label

    def get_time(self):
        return self.t

# set vars to class using constructor
var1 = TimeStamp()
var2 = TimeStamp()

print(var1.get_time()) # call auto sets property of the class to current time
print(var2.get_time()) # then passes that variable to get_time
print

print(var1.get_time())
print(var2.get_time())
