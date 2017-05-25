import pprint

mydict = {}
fh = open('../script_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')
    mydict[id] = state # init dict with vals

pprint.pprint(mydict)
#print(mydict['ak9'])
