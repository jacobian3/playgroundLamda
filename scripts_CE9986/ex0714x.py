import pprint

outer_list = []
filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')
    
    # list ot dict case: create sequence of key:val pairs and assign
    # this has the effect of groupin them together. This could have also been
    # achieved by appending an empty dictionary using **dict notation
    inner_dict = {'city':city, 'id':idnum, 'state':state}
    outer_list.append(inner_dict) # place the inner dict inside of the list

pprint.pprint(outer_list)
