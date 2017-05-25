import pprint
filename = '../script_data/student_db.txt'

def getlines(filename):
    mylist = []

    for items in open(filename).readlines()[1:]:
        items = items.rstrip()
        mylist.append(items)

    pprint.pprint(mylist)

getlines(filename)
