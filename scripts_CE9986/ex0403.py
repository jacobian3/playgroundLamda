mylist = []

file = "/Users/jacobian3/version-control/tabula_rasa/script_data/student_db.txt"

for line in open(file).readlines():
    line = line.rstrip().split(":")
    mylist.append(line[3])
print(mylist)
