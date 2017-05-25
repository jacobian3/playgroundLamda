# EXAMPLE 3.9
SEL_YEAR = '1928'

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
        line = line.split()[1]
        print(line)

