filename = "/Users/jacobian3/version-control/tabula_rasa/script_data/pyku.txt"
checktext = "we're certainly out of gouda but Python is great."

fh_set = set()

fh = open(filename).read().split() # list is an iterable

for word in fh:
    word = word.rstrip(';.!').lower()
    fh_set.add(word)    

for word in checktext.split():
    if word not in fh_set:
        print(word)
