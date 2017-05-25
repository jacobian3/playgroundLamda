#test message
msg = 'I am happy or sad or angry or mad or generous or stingy.'

print("test message string: " + msg)
print()
string_search = input("Enter a word in the test message to search: ")

word_count = msg.count(string_search)

print("There are/is {} words called: '{}'.".'format(word_count, string_search))

