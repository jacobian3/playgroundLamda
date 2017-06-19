import datetime

class TimeStamp(object):
    """ store the current timestamp in an instance"""
    def set_time(self):
        self.t = str(datetime.datetime.now()) # t is attribute label

    def get_time(self):
        return self.t

var1 = TimeStamp()
var2 = TimeStamp()

var1.set_time()
var2.set_time()

print(var1.get_time())
print(var2.get_time())
print
var1.set_time()

print(var1.get_time())
print(var2.get_time())
