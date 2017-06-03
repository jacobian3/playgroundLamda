sentence = "I could; I wouldn't. I might? Might I!"
wordset = set() 
for item in sentence.split():
    item = item.rstrip(";?!").lower()
    wordset.add(item)
print(wordset)
