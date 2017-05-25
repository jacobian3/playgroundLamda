mydict = dict( zip( 'c b a'.split(),[0.3, 7, 5] ) )

for key in sorted(mydict, key=mydict.get, reverse=True):
    print('{} => {}'.format(key, mydict[key]))
