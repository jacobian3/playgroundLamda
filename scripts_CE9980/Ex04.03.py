import pprint

# ??? how does this work?
#pp = pprint.PrettyPrinter(indent=4) # will print the list so easier 2 read

mylist = []

fh = open('../script_data/student_db.txt')

for line in fh:
    line = line.split(':')
    mylist.append(line)
#mylist.pop(0) # removes the first element of the list (column headings)
pprint.pprint(mylist)

