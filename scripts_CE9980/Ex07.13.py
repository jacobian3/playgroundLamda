# Building a list of list
import pprint

outer_list = [] # no need to initialize inner_list b/c done in loop
fh = open('../script_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id_num, street, city, state, zipcode = line.split(':')

    #initialize items to a inner_list with values
    inner_list = [id_num, city, state] 
    outer_list.append(inner_list)

pprint.pprint(outer_list)
print()
print(outer_list[0][1])

