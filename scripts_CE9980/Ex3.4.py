# EXAMPLE 3.4

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    line = line.rstrip()[:4]
    print(line)
    

