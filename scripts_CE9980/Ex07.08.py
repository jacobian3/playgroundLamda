words = 'Hello my dear the heart is a child'.split()

long_words = [ word.upper() for word in words if len(word) > 3 ]

print(long_words)
