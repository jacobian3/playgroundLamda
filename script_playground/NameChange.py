#EXAMPLE
import os

fh = open('./script_data/name_change.txt')

for line in fh:
    line = line.rstrip()[8:]
    line = 'Notes' + line
    print(line)

