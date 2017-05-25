import pprint
filename  = '../script_data/student_db.txt'


file_contents = [ line.rstrip() for line in open(filename).readlines()[1:]]
pprint.pprint(file_contents)


