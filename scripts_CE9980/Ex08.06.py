#!/usr/bin/env python

import sys
import os

# STEP 1
# validate directory name from the user at the CLI 
try:
    #dirname = sys.argv[1]
    dirname = '../script_data' #test of existing dir/file
    #dirname = '../script_dataxxxnonexistxxx' # test of non-existing dir/file
except IndexError:
    exit("error: please provide an argument")

# STEP 2
# validate directory existance
try:
    files = os.listdir(dirname) #assigns a list of files in given directory
except IOError:
    exit("error: directory doesn't exist or is not readable")

# STEP 3
# loops through each list filename item
for filename in files:
    # joins and assigns ea. filename with its respective dirname (given @ CLI)
    # this is a relpath
    full_path = os.path.join(os.path.abspath(dirname), filename)
    # STEP 4
    # test for file/directory type
    if os.path.isfile(full_path):
        this_type = 'file'
    else:
        this_type = 'dir'

    # STEP 5 
    # set file size 
    file_size = os.path.getsize(full_path) # just gets the size of the abspath

    # STEP 6 : write result
    print("{} ({}: {})".format(filename, this_type, file_size))
