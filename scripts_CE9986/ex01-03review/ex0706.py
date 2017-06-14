filename = '../script_data/revenue.txt'

#print(open(filename).readlines()[0:3]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

fh = open(filename).readlines()

# Though, split converts line into a split, this is only used for sorting
# the sorted list is a list of strings. Therefore, line is a string.
for line in sorted(fh, key=lambda line: float(line.split(',')[-1])):
    line = line.rstrip() # rstrip method can be used b/c line rtn's a string
    print(line)
