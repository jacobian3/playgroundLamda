# EXAMPLE 3.3
counter = 0

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    counter += 1
    print(counter, line, end = "")

print('total files read: {}'.format(counter))
