filename = '../script_data/pyku.txt'

#print(open(filename).readlines()[0:2]) #4DEBUGGING
#print(open(filename).readlines()[-1])
#exit()

def by_num_words(line): # 2nd the value to be sorted
    words = line.split() # 3rd process and return values
    return len(words)

# 1st: lines from the file are to be sorted
for line in sorted(open(filename).readlines(), key=by_num_words):
    line = line.rstrip()
    print(line)

print('using lambda below')

for line in sorted(open(filename).readlines(), key=lambda line:len(line.split())):
    line = line.rstrip()
    print(line)


