# summing dictionary
mydict = {}

fh = open('../script_data/revenue.txt')

lines = fh.readlines()

for line in lines:
    line = line.rstrip()
    names,state,num = line.split(',')

    if state not in mydict:
        mydict[state] = 0
    mydict[state] += float(num)

print(mydict)
