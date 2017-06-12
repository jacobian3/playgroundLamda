filename = '../script_data/revenue.txt'

#print(open(filename).readlines()[0:3]) #debug file
#print(open(filename).readlines()[-1])
#exit()

mydict = {} 

for line in open(filename).readlines():
    name, state, price = line.split(",")
    if state not in mydict:
        mydict[state] = 0
    mydict[state] += float(price)

sorted_keys = sorted(mydict, key=mydict.get)

for key in sorted_keys:
    print("{} => {}".format(key, mydict[key]))
