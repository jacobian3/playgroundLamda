mydict = {'c': 0.3, 'b': 7, 'a': 5} 

print("Enter: 'assending or decending'\n")
unput = input("please enter a direction: " )

if unput == 'assending':
    toggle = False

else:
    toggle = True
    
sorted_keys = sorted(mydict, key=mydict.get, reverse=toggle)

for key in sorted_keys:
    print("{} => {}".format(key, mydict[key]))
