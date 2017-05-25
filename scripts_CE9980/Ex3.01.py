import os
##DEBUG OF CWD AND LIST OF CONTENTS
#
##change directory -> test file dir
#os.chdir( '/Users/jacobian3/version-control/tabula_rasa/script_data' )
#
##debug to see current directory
#print( os.getcwd() )
#
## debug contents of the current directory
#print( os.listdir( '../script_data' ) )

## EXAMPLE OF CONVOLUTED LOGIC FILTERING
#fh = open( '../script_data/FF_abbreviated.txt' )
#
#for line in fh:
#    if not int(line.split()[0][:4]) < 1928 and not float(line.split()[1]) < 1:
#        line = line.rsplit()
#        print(line)

# ACTUAL EX3.1 

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    print(line)
