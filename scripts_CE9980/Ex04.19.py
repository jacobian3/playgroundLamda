fh = open('../script_data/pyku.txt')
word_set = set()

lines = fh.read()

word_list = lines.split() # creates a list of words

for word in word_list:
    word = word.strip(',.').lower()
    word_set.add(word)

print(word_set)
print(len(word_set))
