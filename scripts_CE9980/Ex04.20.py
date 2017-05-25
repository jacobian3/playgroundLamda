text = "We're certainly out of gouda but Python is great."
fh = open('../script_data/pyku.txt')
word_set = set()

lines = fh.read()

word_list = lines.split() # creates a list of words

for word in word_list:
    word = word.strip(',.').lower()
    word_set.add(word)

test_words = text.lower().split() # str -> list w/o strip:b/c no spec chrs

for word in test_words:
    if word not in word_set:
        print(word)


