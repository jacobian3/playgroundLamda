import os
import sys

#try:
#    dirname = sys.argv[1]
#except IndexError:
#    exit('error: please provide argument')

dirname = '../script_data/' # 4DEBUGGING

try:
    files = os.listdir(dirname)
except IOError:
    exit('error: directory does not exist or is not readable'.format(dirname))

for filename in files:
    full_path = os.path.join(dirname, filename)
    if os.path.isfile(full_path):
        this_type = 'file'
    else:
        this_type = 'dir'

    print('{} ({})'.format(filename, this_type))
