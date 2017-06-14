sentence = "I could; I wouldn't. I might? Might I!"

for item in sentence.split():
    item = item.rstrip(";?!").lower()
    print(item)
