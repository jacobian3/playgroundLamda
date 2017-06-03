counter = 0
file = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(file).readlines():
    print(line)
    counter += 1

print(counter)
