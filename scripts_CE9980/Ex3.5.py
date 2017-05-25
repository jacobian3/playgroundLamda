# EXAMPLE 3.5

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    if line[:4] == '1928':
        print(line)
    

