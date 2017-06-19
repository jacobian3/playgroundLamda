import pprint

filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

outer_dict = {}

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')

    if state not in outer_dict:
        # like a summing dictionary: init list
        outer_dict[state] = [] # {'state' : []}; this dict is the empty list
    outer_dict[state].append(idnum) # since it is a list, it can be appended!

pprint.pprint(outer_dict)
print()
print(outer_dict['ak9']['state'])
print(outer_dict['NJ']['state'])
