mydict = dict( zip( 'c b a'.split(),[0.3, 7, 5] ) )

## play with lambdas 
#for key in sorted(mydict, key=lambda num: mydict[num]):
#    print('{} => {}'.format(key, mydict[key]))

for key in sorted(mydict, key=mydict.get):
    print('{} => {}'.format(key, mydict[key]))
