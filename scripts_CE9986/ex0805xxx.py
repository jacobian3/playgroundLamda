import os
import sys

# STEP 1: get directory from the user
try: 
    dirname = sys.argv[1]
except IndexError:
    exit("No directory was entered")

# STEP 2: List files in the directory
try:
    files = os.listdir(dirname)
except FileNotFoundError:
    exit("The directory isn't valid")
    
# STEP 3: Loop throught each file in the list of files 
for filename in files:
    #STEP 4: Pair each filename with the reletive directory
    full_path = os.path.join(dirname, filename)
    #STEP 5 verify if file or directory
    if os.path.isfile(full_path):
        this_type = "file"
    else:
        this_type = "dir"

    print("{} ({})".format(filename, this_type))
