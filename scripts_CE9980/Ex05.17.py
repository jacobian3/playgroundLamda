import pprint
mydict = {} 

fh = open('../script_data/revenue.txt')

for lines in fh:
    name, state, number = lines.split(',')

    if state not in mydict:
        mydict[state] = 0
    mydict[state] += float(number)

my_sorted_dict = sorted(mydict, key=mydict.get)

for key_item in my_sorted_dict:
    print("{} => {}".format(key_item, mydict[key_item]) )
