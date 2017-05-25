# EXCERCISE 3.13

counter = 1
floatsum = 0
floatsum_list = [] #used to double check my thought process

SEL_YEAR = '1928'

fh = open( '../script_data/FF_abbreviated.txt' )

for line in fh:
    if line[:4] == SEL_YEAR:
        line = line.split()[1]
        new_line = float(line)
        print(counter, new_line)

        #counters
        floatsum_list.append(new_line) #used to double check my thought process
        floatsum += new_line
        counter += 1

print('The total of column 2: {}'.format(floatsum))
print(floatsum_list,'list_total: ',sum(floatsum_list))
