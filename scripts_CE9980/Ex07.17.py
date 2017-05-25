#COUNTING DICTIONARY

mydict = {}
fh = open('../script_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id_num, street, city, state, zipcode = line.split(':')

    #counter and conditions
    if state not in mydict:
        mydict[state] = 0
    mydict[state] += 1

print(mydict)
print()
print(mydict['NY'])
