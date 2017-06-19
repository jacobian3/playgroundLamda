counter = 0

file = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(file).readlines():
    counter += 1
    print(counter,line)

print(counter)
