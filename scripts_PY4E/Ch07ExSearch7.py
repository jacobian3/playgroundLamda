fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ',fname)
    exit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("Subject:"):
        print(line)
        count += 1
print("There were", count, "subject lines in", fname)
