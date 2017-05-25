#EX. 2.10

#test message
msg = 'I am happy or sad or angry or mad or generous or stingy.'
print("test message string: " + msg)
print()
search_string = input("Enter a character to replace: ")

new_str = msg.replace(search_string, 'x')

print("The new string: " + new_str)

