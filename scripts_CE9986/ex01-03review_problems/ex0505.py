mydict = dict()

for word in 'Hey there I am amazing!'.split():
    mydict[word] = len(word)

uinput = input('please enter a word: ')

if uinput in mydict:
    print('the word "{}" is len {}'.format(uinput, mydict[uinput]))
else:
    print('the word "{}" does not exit in the dictionary.'.format(uinput))
