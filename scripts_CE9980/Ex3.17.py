# EXAMPLE 3.17

FILENAME = '../script_data/pyku.txt' 

fh = open(FILENAME) 

text = fh.read() # method read takes the entire file 

line = text.split() #splits on whitespace; not on '\n'

print(line)
print(type(line))
print(line[0])
print(line[-1])

