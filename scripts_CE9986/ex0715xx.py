import pprint

filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

outer_dict = {}

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')

    # we can't use: outer_dict = { idnum:state } b/c there isn't another
    # structure to store the key:value pair like the previous problem
    # therefore each time the loop is run the outer_dict wll be overwriten by 
    # the new key:value pair. Therefore we use an assingment to do it
    # state => idnum vs outer_dict being assigned and destroyed ea. time
    outer_dict[idnum] = state 

pprint.pprint(outer_dict)
print(outer_dict['ak9'])


