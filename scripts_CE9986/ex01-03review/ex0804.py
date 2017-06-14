import sys
import os

file_name =  sys.argv[1]

if os.path.isfile(file_name):
    print("{}: {} bytes".format(file_name, os.path.getsize(file_name)))

else:
    print('error: {} is not a file in this directory'.format(file_name))


