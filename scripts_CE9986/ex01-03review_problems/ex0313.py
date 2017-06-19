floatsum = 0

filea = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(filea).readlines():
    if line[0:4] == '1928':
        line = line.rstrip().split()
        col2 = float(line[1])
        floatsum += col2
print(floatsum)
