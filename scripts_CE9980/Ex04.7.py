revenues = []

fh = open('../script_data/revenue.txt')

for line in fh:
    fields = line.split(',') # for ea. line of string split on coma and return
                            # list of string: ea field
    fval = float(fields[2])
    revenues.append(fval)

print('len of: {} and a sum of: {} is an avg:{}'.format(len(revenues), 
    sum(revenues), sum(revenues) / len(revenues)))
