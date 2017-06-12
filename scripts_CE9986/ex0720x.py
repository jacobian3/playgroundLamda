import pprint

outer_dict = {}
fh = open( '../script_data/revenue.txt' )

for line in fh:
    company, state, revenue = line.split(',')

    # Dict of list: step 1 -> define empty inner_list check
    if state not in outer_dict:
        # set inner_list to an empty list; effectively zero if using
        # summing dictionary as a go-by
        outer_dict[state] = [] # outer_dict is now a list
    # step 2: irrespective of 'state' existance, append to the prior list the 
    # new value
    outer_dict[state].append(float(revenue)) 

#compute average of NY
avg = sum(outer_dict['NY']) / len(outer_dict['NY'])

pprint.pprint(outer_dict)
print()
print(avg)
