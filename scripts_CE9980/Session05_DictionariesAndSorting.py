## BUILD A "COUNTING" OR "SUMMING" DICTIONARY
#state_count = dict()
#
##can do all file handle operations in one line; (1) open (2) read str -> list
## of lines (3) remove 1st list element (contains column heading)
#for line in open('../script_data/student_db.txt').readlines()[1:]:
#
#    # splits line list-> elements list
#    # reads all list elements to vars that match headings
#    id, address, city, state, zip = line.split(':') 
#    print('state: {}'.format(state)) #DEBUG
#
#    if state not in state_count:
#        state_count[state] = 0
#    state_count[state] += 1
#
#for state in state_count:
#    print("{}: {} occurances".format(state, state_count[state]))

## WHAT IS THE KEY TO THE COUNTING/SUMMING DICTIONARY
## the key to making a counting dictionary work is in checking to see if any 
## given key to be counted is new to the dictionary.  If the key is new, it must
## be added to the dictionary.  If it isn't new, it will be rewritten to the 
## dictionary, but with a new value that is (in this case) one more than the 
## value it held earlier.)
