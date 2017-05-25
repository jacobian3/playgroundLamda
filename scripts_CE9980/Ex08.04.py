import os
import sys

try:
    filename = sys.argv[1]
    #filename = '../script_data/student_db.txt'

    if os.path.isfile(filename):
        print("{}: {} bytes".format(filename, os.path.getsize(filename)))

    else:
        print("error: {} is not a file in this directory".format(sys.argv[0]))

except IndexError:
    exit('error: two args MUST be entered')
