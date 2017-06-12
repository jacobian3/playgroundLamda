filetype = '../script_data/revenue.txt'

mydict = {}

for line in open(filetype).readlines():
    name, state, price = line.rstrip().split(',')
    if state not in mydict:
        mydict[state] = 0.0
    mydict[state] += float(price)

print(mydict)
