mydict = dict( zip( 'c b a'.split(),[0.3, 7, 5] ) )

while True:

    unput = input("please enter a direction(assending/decending): ")

    if unput == 'assending':
        rev = False
        break
    if unput == 'decending':
        rev = True
        break
    else:
        print("Enter 'assending' or 'decending'")

for key in sorted(mydict, key=mydict.get, reverse=rev):
    print('{} => {}'.format(key, mydict[key]))
