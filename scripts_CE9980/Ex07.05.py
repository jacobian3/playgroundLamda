pyku = '../script_data/pyku.txt'

fh = open(pyku).readlines()
print(fh,"\n")

for line in sorted(open(pyku).readlines(), key=lambda line: len(line.split())):
    line = line.rstrip()
    print(line)
