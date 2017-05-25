## UNDERSTADING HOW DATETIME WORK
#import datetime
#
#dt = datetime.date.today()
#
#print(dt)



## UNDERSTADING CSV
import csv

fh = open('../script_data/students.txt')
reader = csv.reader(fh) # we call on reader attribute cvs a method reader
for record in reader:
    print('{}-{},{}'.format(record[0],record[2],record[1])
