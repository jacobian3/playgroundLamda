import pprint

outer_list = []
fh = open('../script_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id_num, street, city, state, zipcode = line.split(':')
    outer_list.append(id_num)

print(outer_list)
print(outer_list[0])
