file = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(file).readlines():
    line = line.rstrip()[0:4]
    print(line)

