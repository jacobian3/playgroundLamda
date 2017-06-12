mydict = dict(zip('a b c'.split(),[1, 2, 3]))

#newdict = dict(zip('e f'.split(),[4, 5])) 
#expected_dict = {**mydict, **newdict} # 3.5 way to merge dictionaries
#print(expected_dict)

mydict['e'] = 4
mydict['f'] = 5

print(mydict)
