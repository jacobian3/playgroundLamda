import pprint

outer_dict = {}
filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')

    # The difference in the prior ex0714 is that the inner_dict assign
    # step was destructive. It didn't appear this way, however, because its val
    # was appended to an existing list; stored. Without this intermediate step
    # the dictionary assignment would continuously be destroyed.
    outer_dict[id] = state 

pprint.pprint(outer_dict)
