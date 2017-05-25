## Ex. 2.8
##SET counter 
#or_count = 0
#
##starter code:
#msg = 'I am happy or sad or angry or mad or generous or stingy.'
#
##convert string into a list
#my_msg = msg.split()
#
#for item in my_msg: # iterate through the sequence
#    if item == 'or':
#        #count number of times
#        or_count += 1
#
#print("There are {} letter 'or's.".format(or_count))

#BOOK SOLUTION

#starter code:
msg = 'I am happy or sad or angry or mad or generous or stingy.'

string_search = 'or'

or_count = msg.count(string_search)

print("There are {} letter 'or's.".format(or_count))

