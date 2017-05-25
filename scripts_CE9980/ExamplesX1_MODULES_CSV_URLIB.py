## UNDERSTADING HOW DATETIME WORK
#import datetime
#
#dt = datetime.date.today()
#
#print(dt)


## UNDERSTADING CSV
#import csv
#
#fh = open('../script_data/students.txt') # "r" isn't needed for read
#reader = csv.reader(fh) # we call on reader attribute cvs a method reader
#for record in reader:
#    print('{} - {}, {}'.format(record[0],record[2],record[1]))


# EXAMPLE URLB MODULE
import urllib.request # built in replacement for request module
my_url = 'http://www.google.com'
readobj = urllib.request.urlopen(my_url)
text = readobj.read()
print(text)
readobj.close()

#for line in readobj.readline():
#    print(line)
#readobj.close()
