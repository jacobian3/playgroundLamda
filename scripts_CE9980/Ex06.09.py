def by_num_words(arg):
    line = arg.split()
    return len(line)

fh = open('../script_data/pyku.txt')
lines = fh.readlines()
for line in sorted(lines,key=by_num_words):
    line = line.rstrip()
    print(line)
