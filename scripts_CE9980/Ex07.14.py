# Building a list of dicts
import pprint

outer_list = [] # no need to initialize inner_dict b/c done in loop
fh = open('../script_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id_num, street, city, state, zipcode = line.split(':')

    #initialize items to a inner_dict
    # my initial first approach
    #inner_dict = dict( zip( ['id', 'city', 'state'],[id_num, city, state] ) ) 
    
    # more eloquent book approach
    # initialize inner_dict with key:val pairs
    inner_dict = {'id': id_num, 'city': city, 'state': state }
    outer_list.append(inner_dict)

pprint.pprint(outer_list)
print()
