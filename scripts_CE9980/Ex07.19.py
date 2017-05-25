# SUMMING DICTIONARY

state_rev_dict = {}
fh = open('../script_data/revenue.txt')

for line in fh:
    company, state, revenue = line.split(',')

    #summing dictionary
    if state not in state_rev_dict:
        state_rev_dict[state] = 0.0
    state_rev_dict[state] += float(revenue)

print(state_rev_dict)
print()
print(state_rev_dict['NJ'])


