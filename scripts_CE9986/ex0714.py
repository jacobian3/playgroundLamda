import pprint

filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

outer_list = []

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')

    inner_dict = {'idnum':idnum, 'city':city, 'state':state}
    outer_list.append(inner_dict)

pprint.pprint(outer_list)
