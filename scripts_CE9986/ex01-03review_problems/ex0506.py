filename = '../script_data/revenue.txt'

#print(open(filename).readlines()[0:2]) # debugging 
#print(open(filename).readlines()[-1])

mydict = {}

for line in open(filename).readlines():
    price  = line.split(',')[2]
    name  = line.split(',')[0]
    mydict[name] = price
print(mydict)
