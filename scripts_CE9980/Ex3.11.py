# EXCERCISE 3.11

SEL_YEAR = '1928'

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    if line[:4] == SEL_YEAR:
        line = line.split()[1]
        print(line, float(line) * 2)
