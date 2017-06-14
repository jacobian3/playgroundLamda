filename = '../script_data/student_db.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()[1:]

line_list = [line.rstrip() for line in fh]

print(line_list)
