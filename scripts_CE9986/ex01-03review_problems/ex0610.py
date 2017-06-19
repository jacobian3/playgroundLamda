filename = '../script_data/revenue.txt'

#print(open(filename).readlines()[0:2]) #debug
#print(open(filename).readlines()[-1])

def by_num(line): # 2nd: value to sort is "by_num"
    name, state, price = line.split(',') # 3rd process and return
    return float(price)

# 1st: sort list of items (lines from file)
for line in sorted(open(filename).readlines(), key=by_num):
    line = line.rstrip()
    print(line)
