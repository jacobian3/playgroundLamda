import pprint
mydict = {} 

fh = open('../script_data/revenue.txt')

for lines in fh:
    name, state, number = lines.split(',')
    mydict[name] = number

pprint.pprint(mydict)
