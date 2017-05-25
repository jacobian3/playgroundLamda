lendic = {}
mylist = 'Hey there I am amazing!'.split()

for word in mylist:
    lendic[word] = len(word)

word = input("please enter a word: ")

if word in lendic:
    print('the word "{}" is len {}.'.format(word,lendic[word]))
else:
    print('the word "{}" does not exist in the dictionary.'.format(word))
