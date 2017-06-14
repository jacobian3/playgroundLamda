import os
import sys

#try:
#    dir = sys.argv[1] # STEP 1. get directory from the user
#except IndexError:
#    exit("missing arguments; try again")

dir = "../script_data" # for debugging

try:
    files = os.listdir(dir) # STEP 2. list all files from STEP 1.
except FileNotFoundError:
    exit("There is no directory by that name")

for filename in files: # STEP 3. loop through all files listed
    #STEP 4 and 5: you must check the rel/abs path to get dir/file info
    full_path = os.path.join(dir, filename) # STEP 4. join ea. dir and filename
    if os.path.isfile(full_path): # STEP 5. Check to see if file
        this_type = "file"
    else: # STEP 5. Else, is dir
        this_type = "dir"
    # STEP 6: write the filename and the file type
    print("{} ({})".format(filename, this_type))
