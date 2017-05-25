sentence = "I could; I wouldn't. I might? Might I!"

words = sentence.split() # string -> list

for word in words:
    word = word.rstrip('?.!;') # strips ending arg vals
    print(word)
