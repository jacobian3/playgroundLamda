# EXAMPLE 3.6
counter = 0
fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    if line[:4] == '1928':
        print(line)
        counter += 1

print('total files read: {}'.format(counter))
