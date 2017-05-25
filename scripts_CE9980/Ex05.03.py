lendic = {}
mylist = 'Hey there I am amazing!'.split()

for word in mylist:
    lendic[word] = len(word)

# to practice sorting by value
sort_len_dict = sorted(lendic, key=lendic.get)

for key in sort_len_dict: # sorted produces a list
    print('"{}" is len {}.'.format(key,lendic[key]))
    
