revenue = '../script_data/revenue.txt'

fh = open(revenue).readlines()
print(fh,"\n")

for line in sorted(open(revenue).readlines(), key=lambda line: float(line.split(',')[-1])):
    line = line.rstrip()
    print(line)
