revenues = []

fh = open('../script_data/revenue.txt')

for line in fh:
    fields = line.split(',') # for ea. line of string split on coma and ret a 
                            # list of string: ea field
    fval = float(fields[2])
    revenues.append(fval)

print(revenues)
print(sum(revenues))
