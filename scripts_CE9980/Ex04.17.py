sentence = "I could; I wouldn't. I might? Might I!"
s_set = set()

words = sentence.split() # string -> list

for word in words:
    word = word.rstrip('?.!;').lower() # strips ending arg vals
    s_set.add(word)
    #word = word.lower() # method converts object case

print(s_set)
