# EXAMPLE 3.8

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    line = line.split()[0]
    print(line)
