mylist = []

file = "/Users/jacobian3/version-control/tabula_rasa/script_data/revenue.txt"

for line in open(file).readlines():
    name, state, price = line.rstrip().split(',')

    mylist.append(float(price))

print(round(sum(mylist) / len(mylist), 2))
