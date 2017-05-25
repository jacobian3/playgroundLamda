def by_last(arg):
    name, state, dollar = arg.split(',')
    return float(dollar)
    
fh = open('../script_data/revenue.txt')
lines = fh.readlines()
for line in sorted(lines, key=by_last):
    line = line.rstrip()
    print(line)


