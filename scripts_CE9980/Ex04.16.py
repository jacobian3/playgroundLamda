
sentence = "I could; I wouldn't. I might? Might I!"

words = sentence.split() # string -> list

for word in words:
    word = word.rstrip('?.!;').lower() # strips ending arg vals
    #word = word.lower() # method converts object case
    print(word)
