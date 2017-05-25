fh = open('../script_data/pyku.txt')

lines = fh.read()

word_list = lines.split() # creates a list of words

for word in word_list:
    print(word)
