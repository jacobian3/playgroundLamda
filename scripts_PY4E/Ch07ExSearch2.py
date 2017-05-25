fh = open('mbox-short.txt')
count = 0
for line in fh:
    count += 1
    if line.startswith('From:'):
        print(line.rstrip())
print('count: ', count)
