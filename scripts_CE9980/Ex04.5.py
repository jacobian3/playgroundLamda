mylist = []

fh = open('../script_data/student_db.txt') # open file and return file object

for line in fh:
    line = line.split(':')
    if line[3] == 'NY':
        mylist.append(line[0])
print(mylist)
