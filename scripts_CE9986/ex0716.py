import pprint

filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

outer_dict = {}

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')


    inner_dict = {'street': street, 'city': city, 'state': state, 'zip': zipnum}
    outer_dict[idnum] = inner_dict

pprint.pprint(outer_dict)
print()
print(outer_dict['ak9']['state'])
