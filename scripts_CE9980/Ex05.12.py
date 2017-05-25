
mydict = dict( zip( 'c b a'.split(),[0.3, 7, 5] ) )

for key in sorted(mydict):
    print('{} => {}'.format(key, mydict[key]))
