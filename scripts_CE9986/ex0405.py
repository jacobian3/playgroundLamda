mylist = []

file = "/Users/jacobian3/version-control/tabula_rasa/script_data/student_db.txt"

for line in open(file).readlines()[1:]:
    id_num, street, city, state, zipnum  = line.rstrip().split(":")
    if state == 'NY':
        mylist.append(id_num)
print(mylist)
