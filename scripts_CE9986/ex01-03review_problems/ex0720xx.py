""" build a dict of list """

filename = '../script_data/revenue.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()

mydict = {}

for line in fh:
    name, state, rev = line.split(',')
    if state not in mydict:
        mydict[state] = [] # mydict takes an empty list as a value
    mydict[state].append(float(rev)) #get list from state key; add floats vals

print(mydict,"\n")
print(sum( mydict['NY'] ) / len( mydict['NY'] ))
