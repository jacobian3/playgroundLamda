file = "/Users/jacobian3/version-control/tabula_rasa/script_data/revenue.txt"

for line in open(file).readlines():
    line = line.rstrip()
    print(line)

