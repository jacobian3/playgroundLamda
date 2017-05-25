## TRY/EXCEPT PRACTICE
#import sys
#
#try:
#    firstarg = sys.argv[1]
#    secondarg = sys.argv[2]
#
#    firstarg = int(firstarg)
#    secondarg = int(secondarg)
#except ( IndexError,ValueError ): # trapping multi exceptions 
#    exit('error: two int args MUST be entered')
#
##firstarg = input("Enter argument 1: ")
##secondarg = input("Enter argument 1: ")
##print('{} and {} are the args'.format(firstarg, secondarg)
    

# OS.WALK PRACTICE 
# this configuration works like 'find' command
import os

# NOTE: currently set to give abspath with multiple subfolders
root_dir = os.path.abspath('..') # give absolute path up2 'stop point': arg val

for roots, dirs, files in os.walk(root_dir):
    print(roots)
    for file in files:
        print(os.path.join(roots, file))
