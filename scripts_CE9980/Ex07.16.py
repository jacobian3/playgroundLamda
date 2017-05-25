# BUILD A DICT OF DICTS
import pprint

outer_dict = {}
lines = open('../script_data/student_db.txt').readlines()[1:]

for line in lines:
    line = line.rstrip()
    id_num, street, city, state, zipcode = line.split(':')

    inner_dict = {'street': street, 'city': city, 'state': state, 'zip': zipcode}
    outer_dict[id_num] = inner_dict

pprint.pprint(outer_dict)
#print(outer_dict) # to visualize non pprint
