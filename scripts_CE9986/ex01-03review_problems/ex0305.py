file = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(file).readlines():
    line.rstrip()[0:4]
    if line.rstrip()[0:4] == '1928':
        print(line)

