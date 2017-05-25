# dict of list (floats)

state_rev_dict = {}
fh = open('../script_data/revenue.txt')

for line in fh:
    company, state, revenue = line.split(',')

    #summing dictionary
    if state not in state_rev_dict:
        state_rev_dict[state] = []
    state_rev_dict[state].append(float(revenue))

print(state_rev_dict)
print()
print(sum(state_rev_dict['NY']) / len(state_rev_dict['NY']))


