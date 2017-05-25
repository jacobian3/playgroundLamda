# 3 DATA STREAMS IN UNIX / WINDOWS
# 
# process: a running program
#    - has a PID (process ID)
#    - allocates memory with permissionis of the OS
#    - may write to STDOUT and/or STDERR
#    - may read/write to files (the disk) 
#    - may make a newtwork conneciton (over socket)
#
# ALL BELOW = DATA STREAMS!
# STDIN (standard in)
# STDOUT (standard out)
# STDERR (standard error)


import os


#print(dir(os))


print(os.getcwd())
