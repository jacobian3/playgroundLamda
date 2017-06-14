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
    #STEP 4.1: get the size of each file
    file_size = os.path.getsize(full_path)
    #STEP 5 verify if file or directory
    if os.path.isfile(full_path):
        this_type = "file"
    else:
        this_type = "dir"

    print("{} ({}) {}: in bytes. ".format(filename, this_type, file_size))
