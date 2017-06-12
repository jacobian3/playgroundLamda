filename = '../script_data/revenue.txt'

mydict = {}

for line in open(filename).readlines():
    name, state, price  = line.rstrip().split(',')
    mydict[name] = price
print(mydict)
