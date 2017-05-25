lendic = {}
mylist = 'Hey there I am amazing!'.split()

for word in mylist:
    lendic[word] = len(word)

sdict = sorted(lendic, key = lendic.get)

print(lendic)

for key in sdict:
    print("keys: ",key,"value: ",lendic[key])

for key in sdict:
    print("key: {} \t value: {}".format(key,lendic[key]))
    
