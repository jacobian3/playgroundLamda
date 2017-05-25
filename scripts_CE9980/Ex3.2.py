# EXAMPLE 3.2

counter = 0

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    print(line, end = "")
    counter += 1

print('total files read: {}'.format(counter))
