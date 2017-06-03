counter = 0

filea = "/Users/jacobian3/version-control/tabula_rasa/script_data/FF_abbreviated.txt"

for line in open(filea).readlines():
    if line[0:4] == '1928':
        counter += 1

        line = line.rstrip().split()
        col2 = float(line[1])
        mycol = 2 * col2

        print(col2, mycol)
print("There are {} items.".format(counter)) # test 
