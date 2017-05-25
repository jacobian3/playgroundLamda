mydict = {}

fh = open('../script_data/student_db.txt')

lines = fh.readlines()[1:]

for line in lines:
    idno,address,city,state,zipno = line.split(':')

    if state not in mydict:
        mydict[state] = 0
    mydict[state] += 1

print(mydict)
