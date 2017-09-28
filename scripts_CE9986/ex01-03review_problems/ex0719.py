filename = '../../script_data/revenue.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()

mydict = {}

for line in fh:
    name, state, rev = line.split(',')
    if state not in mydict:
        mydict[state] = 0.0
    mydict[state] += float(rev)

print(mydict,"\n")
print(mydict['NJ'])
