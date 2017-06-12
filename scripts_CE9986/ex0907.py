import pprint

line_list = []

def getlines(filename):
    for line in open(filename).readlines():
        line_list.append(line)
    return line_list

pprint.pprint(getlines('../script_data/student_db.txt'))
