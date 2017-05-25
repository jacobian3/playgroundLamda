# BUILD A DICT OF LIST
import pprint

outer_dict = {}
fh = open('../script_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id_num, street, city, state, zipcode = line.split(':')

    # modify counter and conditions to create structure
    # pay attention to technique!!!
    if state not in outer_dict:
        outer_dict[state] = []
    outer_dict[state].append(id_num)

pprint.pprint(outer_dict)

for idnum in outer_dict['NJ']:
    print(idnum)
