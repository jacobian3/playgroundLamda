#PROGRAM Ex72IsStringPalindrome
rline = []

#READ line from user
line = input("Enter word to check for palindrone: ")

#COMPUTE palindrone check
#PROCESS reverse of string elements
for element in reversed(line):
    rline.append(element)

#PROCESS check for palindrone
#take the elements of the reversed list and join them
rline = "".join(rline)

#compare entered string with reversed string
if rline == line:
    type = "a palindrone"
else:
    type = "not a palindrone"
    
#WRITE if/not palindrome
print("The string entered is %s." % type)

#END
