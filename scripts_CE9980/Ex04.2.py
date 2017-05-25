fh = open('../script_data/passwords.txt')

lines = fh.readlines() # returns a list of strings
newslice = lines[0:3] # this is a slice of a list with the 0 - 2 elements
print(newslice)
