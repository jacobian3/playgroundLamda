# Dict of list

filename = '../../script_data/revenue.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()

outer_dict = {}

for line in fh:
    name, state, rev = line.split(',')
    if state not in outer_dict:
        outer_dict[state] = []
    outer_dict[state].append(float(rev))

print(outer_dict,"\n")
print(sum(outer_dict['NY'])/len(outer_dict['NY']))
