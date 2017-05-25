fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        print(line)
        count += 1
print('There were',count,'subject lines in',fname)

