import pprint

filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

outer_dict = {}

fh = open(filename).readlines()[1:]

for line in fh:
    idnum, street, city, state, zipnum = line.split(':')

    if state not in outer_dict:
        outer_dict[state] = 0
    outer_dict[state] += 1

print(outer_dict)
print()
print(outer_dict['NY'])
