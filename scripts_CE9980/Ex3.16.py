# EXAMPLE 3.16

filename = '../script_data/pyku.txt' 

fh = open(filename) 

text = fh.read() # method read takes the entire file 

line = text.splitlines() #splits on '\n' ; not whitespace
print(line)
print(type(line))
print(line[0])
print(line[-1])
