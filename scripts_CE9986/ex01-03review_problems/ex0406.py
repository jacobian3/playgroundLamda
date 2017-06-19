summ = 0

file = "/Users/jacobian3/version-control/tabula_rasa/script_data/revenue.txt"

for line in open(file).readlines():
    name, state, price = line.rstrip().split(',')

    summ += float(price)

print(round(summ,2))
