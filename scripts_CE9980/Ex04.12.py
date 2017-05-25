fh = open('../script_data/revenue.txt')

for line in fh:
    line = line.rstrip() # remove ' \n ' at end
    print(line) #print will auto-insert a newline chr; no need for 2
