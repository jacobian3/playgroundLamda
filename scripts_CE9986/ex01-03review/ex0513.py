mydict = {'c': 0.3, 'b': 7, 'a': 5} 

sorted_keys = sorted(mydict, key=mydict.get)

for key in sorted_keys:
    print("{} => {}".format(key, mydict[key]))
