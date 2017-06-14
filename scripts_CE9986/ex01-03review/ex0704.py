line_list = [
    'the value on this line is 333',
    'the value on this line is 3',
    'the value on this line is 1',
    'the value on this line is 2',
]

for line in sorted(line_list, key=lambda line: line.split()[-1]):
    print(line)
