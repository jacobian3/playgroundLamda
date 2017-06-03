filea = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(filea).readlines():
    line = line.rstrip().split()[1] # works from inside out
    print(line)

