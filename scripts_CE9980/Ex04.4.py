import pprint

mylist = []

fh = open('../script_data/student_db.txt') # open file and return file object

lines = fh.readlines()  # read lines => list of strings
data_lines = lines[1:] #!!! excludes the first line; so that no pop()
#pprint.pprint(data_lines) DEBUG

for line in data_lines:
    line = line.split(':')
    mylist.append(line[3])

pprint.pprint(mylist)

