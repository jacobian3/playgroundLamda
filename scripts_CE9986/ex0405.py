""" list of max size """

class MaxSizeList(object):
    """constructs instances that have a list as attribute"""
    def __init__(self, usr_in):
        """set attrib to empty list """
        self.mylist = []
        self.max_size = usr_in # max size of the list

    def push(self, value):
        """manage list elements """
        if len(self.mylist) == self.max_size:
            self.mylist.pop(0) 
        self.mylist.append(value)

    def get_list(self):
        return self.mylist # this part not given in initial problem description


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("ho")
a.push("let's")
a.push("go")

b.push("hey")
b.push("ho")
b.push("let's")
b.push("go")

print( a.get_list() ) # ['ho', 'let's', 'go']
print( b.get_list() ) # ['go']
