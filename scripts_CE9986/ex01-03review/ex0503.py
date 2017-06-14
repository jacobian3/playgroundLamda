mydict = dict()

for word in 'Hey there I am amazing!'.split():
    mydict[word] = len(word)

for key in mydict:
    print('"{}" is len {}.'.format(key, mydict[key])) # print key and val
