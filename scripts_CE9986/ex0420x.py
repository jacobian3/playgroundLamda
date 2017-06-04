filename = "/Users/jacobian3/version-control/tabula_rasa/script_data/pyku.txt"
checktext = "we're certainly out of gouda but Python is great."

newset = set()

fh = open(filename)

filetext = fh.read()
words = filetext.split()

for word in words:
    word = word.rstrip(';.?!')
    word = word.lower()
    newset.add(word)

test_words = checktext.split()

for word in test_words:
    if word not in newset:
        print(word)
