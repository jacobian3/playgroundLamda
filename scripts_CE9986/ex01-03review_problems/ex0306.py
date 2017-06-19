counter = 0

filea = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(filea).readlines():
    if line[0:4] == '1928':
        counter += 1
        print(line)
print(counter)

