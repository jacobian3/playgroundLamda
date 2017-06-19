filename = '../script_data/student_db.txt'

mydict = {}

for line in open(filename).readlines()[1:]:
    idnum,address,city,state,zipcode = line.split(':')
    if state not in mydict: 
        mydict[state] = 0
    mydict[state] += 1

print(mydict)
