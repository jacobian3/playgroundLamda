# EXAMPLE 3.15

FILENAME = '../script_data/pyku.txt' 

search_word = 'spam'

fh = open(FILENAME) 

text = fh.read() # method read takes the entire file 

test_word = text.count(search_word) # count searches for # of times 

print(test_word)
